from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.


def profile(request):
    """ View for users profile """

    profile = get_object_or_404(UserProfile, default_user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Profile')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profile/profile.html'
    context = {
        'form': form,
        'order': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)