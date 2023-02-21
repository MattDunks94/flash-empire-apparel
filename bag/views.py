from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view for shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add specified product to shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'Added {product.name} ({size.upper()}) to \
                        your bag'
                )
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                    request, f'Added {product.name} ({size.upper()}) to \
                        your bag'
                )
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}'
                )
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag.')

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Update specified product quantity in shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to \
                    {bag[item_id]["items_by_size"][size]}'
                )
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}.'
                )
        else:
            bag.pop(item_id)

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove specified product in shopping bag """
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(
                    request, f'Removed {product.name} ({size.upper()}) \
                        from your bag'
                    )
        else:
            bag.pop(item_id)
            messages.success(
                    request, f'Removed {product.name} from your bag'
                    )

        request.session['bag'] = bag

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
