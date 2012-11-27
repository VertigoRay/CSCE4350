from django.forms import ModelForm
from django.shortcuts import render, render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext
from shop.models import *

class ProductAddForm(ModelForm):
    # Auto generated form to create Product model.
    class Meta:
        model = Product

def index(request):
    if 'q' in request.GET:
        variables = RequestContext(request, {
            'title': 'Shop',
            'search': 'You searched for: %r' % request.GET['q'],
            # 'products': get_list_or_404(Product, title__icontains=request.GET['q']),
            'products': Product.objects.filter(title__icontains=request.GET['q']),
        })
    else:
        variables = RequestContext(request, {
            'title': 'Shop',
            'category': Category.objects.all(),
        })
    return render(request, 'shop/index.html', variables)

def category(request, category):
    variables = RequestContext(request, {
        'title':    category,
        'products': get_list_or_404(Product, category__name__exact=category),
    })
    return render(request, 'shop/category.html', variables)

def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product.html', {'product': product})

def product_add(request):
    """
    Create a new Server model.
    """
    if request.method == 'POST':
        form = ProductAddForm(request.POST)
        if form.is_valid():
            # Create a new Server object.
            form.save()
    else:
        form = ProductAddForm()
 
    variables = RequestContext(request, {
        'title': 'Add Product',
        'form': form,
    })
    return render_to_response('shop/product_add.html', variables)