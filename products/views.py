from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Colour
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ A view for viewing all products, including sorting and search queries """

    products = Product.objects.all()
    colours = Colour.objects.all()
    search_query = None
    categories = None
    sort = None
    direction = None

    # Search query
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            # Sorting by name.
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            # Sorting direction.
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            
            products = products.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    # Colour filter.
    colour_id = request.GET.get('colour_id')
    if colour_id:
        products = Product.objects.filter(colour=colour_id)

    context = {
        'products': products,
        'search_term': search_query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'colours': colours,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view for viewing individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ A view for adding products """
    # Gather form POST data and save it if valid.
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product Successfully Added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Unable to add product! Please ensure \
            the form is valid.')
    # If no method, return empty form.
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ A view for editing products """

    product = get_object_or_404(Product, pk=product_id)
    # Collect product form data and save if valid.
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully modified product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Unable to edit product! Please ensure the \
            form is valid.')
    # Return form in original state.
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing product: {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def remove_product(request, product_id):
    """ Remove product from the store """

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} successfully removed!')

    return redirect(reverse('products'))
