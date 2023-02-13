from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ A view for viewing all products, including sorting and search queries """

    products = Product.objects.all()
    search_query = None
    categories = None

    # Search query
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # Filtering products via categories.
            products = products.filter(category__name__in=categories)
            # Filtering categories via name.
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            search_query = request.GET['q']
            if not search_query:
                messages.error(request, "The empire has declined your query,\
                nothing was entered. Please try again.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=search_query) | Q(
                description__icontains=search_query
                )
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': search_query,
        'current_categories': categories,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view for viewing individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
