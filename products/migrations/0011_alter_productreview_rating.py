# Generated by Django 3.2 on 2023-02-26 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_productreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
