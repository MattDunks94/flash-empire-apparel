# Generated by Django 3.2 on 2023-02-24 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_order_postcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_bag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
