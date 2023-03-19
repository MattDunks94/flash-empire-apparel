from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.template.defaultfilters import slugify
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
    """ A view for adding blog posts """

    # If not super user, return error, redirect 'home'.
    if not request.user.is_superuser:
        messages.error(request, 'Only the gods of the empire have permission!')
        return redirect(reverse('home'))

    # Gather form POST data and save it if valid.
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            messages.success(request, 'Blog post Successfully Added!')
            return redirect(reverse('view_post_list'))
        else:
            messages.error(request, 'Unable to add blog post! Please ensure \
            the form is valid.')
    # If no method, return empty form.
    else:
        form = BlogPostForm()

    template = 'blog/add-blog-post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
