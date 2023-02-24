from django.http import HttpResponse


class StripeWH_Handler:
    """ Handles Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handles unexpected, unknown webhook event  """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handles payment_intent.succeeded webhook  """

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Handles payment_intent.payment_failed webhook  """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )