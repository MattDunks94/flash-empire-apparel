from django.shortcuts import render

# Create your views here.


def profile(request):
    """ View for users profile """

    template = 'profile/profile.html'
    context = {}

    return render(request, template, context)