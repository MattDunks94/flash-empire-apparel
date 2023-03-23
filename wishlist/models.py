from django.db import models
from profiles.models import UserProfile
from products.models import Product

# Create your models here.


class Wishlist(models.Model):

    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True
        )
    wished_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True, default=1
        )
    date_added = models.DateTimeField(
        auto_now_add=True, blank=False, null=False
        )

    def __str__(self):
        return f'Wishlist ({self.user_profile})'
