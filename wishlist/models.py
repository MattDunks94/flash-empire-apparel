from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Wishlist(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wished_product = models.ManyToManyField(
        Product, related_name='wishlist_product'
    )

    def __str__(self):
        return self.wished_product


class WishedProduct(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
