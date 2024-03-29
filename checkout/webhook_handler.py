from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """ Handles Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Send the customer a order confirmation email """

        customer_email = order.email
        email_subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        email_body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
        )

    def handle_event(self, event):
        """ Handles unexpected, unknown webhook event  """

        return HttpResponse(
                content=f'Unhandled webhook received: {event["type"]}',
                status=200,
            )

    def handle_payment_intent_succeeded(self, event):
        """ Handles payment_intent.succeeded webhook  """

        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object.
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = stripe_charge.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in shipping details.
        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None

        # Update profile info if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(default_user__username=username)
            # Saving shipping details to profile.
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address_1 = shipping_details.address.line1
                profile.default_street_address_2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        # While loop executing 5 times.
        while attempt < 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address_1__iexact=shipping_details.address.line1,
                    street_address_2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )

                order_exists = True
                # If order is found, break out of with loop.
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        # If order exists, successful response.
        if order_exists:
            # Send order confirmation email to customer
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Unhandled webhook received: {event["type"]} | \
                SUCCESS: Verified order already in database.',
                status=200,
            )
        # Otherwise create order.
        else:
            order = None
            try:
                order = Order.objects.create(
                    user_profile=profile,
                    first_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address_1=shipping_details.address.line1,
                    street_address_2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items(

                        ):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete
                return HttpResponse(
                    content=f'Unhandled webhook received: {event["type"]} | \
                    ERROR: {e}', status=500
                )
        # Send order confirmation email to customer
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]} | \
            SUCCESS: Order created in webhook.', status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Handles payment_intent.payment_failed webhook  """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )
