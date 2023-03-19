from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import BlogPostForm

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


@login_required
def add_blog_post(request):
    """ A view for adding new blog posts """

    if not request.user.is_superuser:
        messages.error(request, 'Only the gods of the empire have permission!')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Unable to add blog post! Please ensure \
            the form is valid.')
    else:
        form = BlogPostForm()

    template = 'blog/add-blog-post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
