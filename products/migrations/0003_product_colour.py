# Generated by Django 3.2 on 2023-02-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230204_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colour',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
