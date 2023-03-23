from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Wishlist
from products.models import Product
from profiles.models import UserProfile

# Create your views here.


@login_required
def view_wishlist(request):
    """ A view for viewing user's wishlist """
    if not request.user.is_authenticated:
        messages.error(request, 'You must be pledged to the empire to be \
        granted a wish. Please login or sign up.')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, default_user=request.user)
    wishlist = Wishlist.objects.filter(user_profile=user)

    context = {
        'wishlist': wishlist
    }

    return render(request, 'wishlist/wishlist.html', context)
