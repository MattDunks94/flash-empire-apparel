from django.shortcuts import render
from .models import Post

# Create your views here.


def view_post_list(request):
    """ A view for all blog posts """

    posts = Post.objects.filter(status=1).order_by('-created_on')
    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)
