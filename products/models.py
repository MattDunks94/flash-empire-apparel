from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True
        )
    name = models.CharField(max_length=200)
    description = models.TextField()
    sku = models.CharField(max_length=200, null=True, blank=True)
    has_size = models.BooleanField(default=False, null=True, blank=True)
    colour = models.ForeignKey(
        'Colour', on_delete=models.SET_NULL, null=True, blank=True
        )
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Colour(models.Model):
    colour = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.colour


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_review'
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='product_review'
        )
    body = models.TextField(
        max_length=250, null=False, blank=False, default=''
        )
    rating = models.IntegerField(null=False, blank=False, default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Review: {self.body} by {self.user}'
