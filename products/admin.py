from django.contrib import admin
from .models import Product, Category, Colour

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'colour',
        'category',
        'price',
    )

    list_filter = (
        'colour',
        'category',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Colour)
