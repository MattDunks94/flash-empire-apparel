from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

# Create your models here.


class UserProfile(models.Model):
    """ User profile model for storing delivery info and order history """

    default_user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
        )
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_street_address_1 = models.CharField(
        max_length=80, null=True, blank=True
        )
    default_street_address_2 = models.CharField(
        max_length=80, null=True, blank=True
        )
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
        )
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country *', null=True, blank=True
        )

    def __str__(self):
        return self.default_user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Creates or updates user profile """

    if created:

        UserProfile.objects.create(default_user=instance)
    # Saves the existing profile
    instance.userprofile.save()
