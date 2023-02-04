from django.db import models

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
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name