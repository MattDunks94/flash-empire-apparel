from django.contrib import admin
from .models import Wishlist

# Register your models here.


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'wished_product',
        'date_added',
    )

    ordering = ('-date_added',)


admin.site.register(Wishlist, WishlistAdmin)
