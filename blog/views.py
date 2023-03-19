from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def view_post_list(request):
    """ A view for all blog posts """

    posts = Post.objects.filter(status=1).order_by('-created_on')
    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def view_post_detail(request, slug):
    """ A view for blog post detail """

    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }

    return render(request, 'blog/blog-post-detail.html', context)
