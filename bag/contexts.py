from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    # if total is less than free delivery threshold, calculate delivery charge.
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # The remaining amount the customer needs to spend for free delivery.
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        total = 0
        free_delivery_delta = 0
    # Total cost including delivery.
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
