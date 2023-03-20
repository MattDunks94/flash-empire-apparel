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


@login_required
def edit_blog_post(request, slug):
    """ A view for editing blog posts """

    # If not super user, return error, redirect 'home'.
    if not request.user.is_superuser:
        messages.error(request, 'Only the gods of the empire have permission!')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    # Collect product form data and save if valid.
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited blog post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Unable to edit blog post! Please ensure the\
            form is valid.')
    # Return form in original state.
    else:
        form = BlogPostForm(instance=post)
        messages.info(request, f'You are editing post: {post.title}')

    template = 'blog/edit-blog-post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)
