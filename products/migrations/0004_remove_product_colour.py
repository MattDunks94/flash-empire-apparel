# Generated by Django 3.2 on 2023-02-04 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_colour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colour',
        ),
    ]
