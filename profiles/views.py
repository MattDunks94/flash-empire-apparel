from django.shortcuts import render, get_object_or_404

from .models import UserProfile

# Create your views here.


def profile(request):
    """ View for users profile """

    profile = get_object_or_404(UserProfile, default_user=request.user)

    template = 'profile/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)