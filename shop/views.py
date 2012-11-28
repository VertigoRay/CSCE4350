from django.forms import ModelForm
from django.shortcuts import redirect, render, render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext
from shop.models import *
from django.db import models

class ProductAddForm(ModelForm):
    # Auto generated form to create Product model.
    class Meta:
        model = Product

def index(request):
    title = 'Shop'
    if 'q' in request.GET:
        variables = RequestContext(request, {
            'title': title,
            'search': 'You searched for: %r' % request.GET['q'],
            # 'products': get_list_or_404(Product, title__icontains=request.GET['q']),
            'products': Product.objects.filter(title__icontains=request.GET['q']),
        })
    else:
        variables = RequestContext(request, {
            'title': title,
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
    title = product.title
    condition = product.get_condition_display()
    print condition
    variables = RequestContext(request, {
        'title': title,
        'product': product,
        'condition': condition,
    })
    return render(request, 'shop/product.html', variables)

def product_add(request):
    title = 'Add Product'
    if request.method == 'POST':
        form = ProductAddForm(request.POST)
        if form.is_valid():
            # Create a new Server object.
            new_product = form.save()
            redirect('/shop/%s/' % new_product.id)
    else:
        form = ProductAddForm()
 
    variables = RequestContext(request, {
        'title': title,
        'form': form,
    })
    return render_to_response('shop/product_add.html', variables)

def watch(request):
    if user.is_active:
        watches = get_list_or_404(WatchList, user_id=user.id)
    else:
        watches = Nothing
    title = product.title
    variables = RequestContext(request, {
        'title': title,
        'watches': watches,
    })
    return render(request, 'shop/watch.html', variables)

def watch_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    title = product.title
    variables = RequestContext(request, {
        'title':    title,
        'products': get_list_or_404(Product, category__name__exact=category),
    })
    return render(request, 'shop/watch.html', variables)

def watch_ignore(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    title = product.title
    variables = RequestContext(request, {
        'title':    title,
        'products': get_list_or_404(Product, category__name__exact=category),
    })
    return render(request, 'shop/watch.html', variables)