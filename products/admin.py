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


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Colour)
