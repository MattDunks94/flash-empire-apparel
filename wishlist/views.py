from django.shortcuts import render
from .models import Wishlist
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def view_wishlist(request):
    """ A view for user's wishlist """

    return render(request, 'wishlist/wishlist.html')