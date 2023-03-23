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


def add_to_wishlist(request, product_id):
    """ A view to add product to user's wishlist """

    if not request.user.is_authenticated:
        messages.error(request, 'You must be pledged to the empire to be \
        granted a wish. Please login or sign up.')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, default_user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # Checks whether added wished_item is already in user's wishlist.
    existing_product = Wishlist.objects.filter(
        wished_product=product,
        user_profile=user
        ).exists()

    if existing_product:
        messages.info(request, f'{product.name} has already been wished for!')
        return redirect(reverse('product_detail', args=[product_id]))
        # Adds wished item to wishlist.
    else:
        wished_item = Wishlist.objects.create(
            user_profile=user,
            wished_product=product
            )
        messages.success(request, f'Your wish for {product.name} has been \
        added to your wishlist!')
        return redirect(reverse('product_detail', args=[product_id]))


def remove_from_wishlist(request, product_id):
    """ A view to remove product from user's wishlist """

    if not request.user.is_authenticated:
        messages.error(request, 'You must be pledged to the empire to be \
        granted a wish. Please login or sign up.')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, default_user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    Wishlist.objects.filter(wished_product=product, user_profile=user).delete()

    messages.success(
        request, f"{product.name} successfully removed from your wishlist."
        )

    return redirect(reverse('wishlist'))
