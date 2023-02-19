from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view for shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add specified product to shopping bag """

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
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
      
    request.session['bag'] = bag

    return redirect(redirect_url)
