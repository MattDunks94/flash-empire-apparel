from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = (
        'lineitem_total',
    )


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdmin,)
    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'grand_total',
        'order_total',
    )

    fields = (
        'order_number',
        'date',
        'delivery_cost',
        'grand_total',
        'order_total',
        'full_name',
        'email',
        'phone_number',
        'postcode',
        'town_or_city',
        'street_address_1',
        'street_address_2',
        'county',
        'country',
    )

    list_display = (
        'order_number',
        'date',
        'full_name',
        'delivery_cost',
        'grand_total',
        'order_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
