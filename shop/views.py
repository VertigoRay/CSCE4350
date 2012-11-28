from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.forms import ModelForm
from django.shortcuts import redirect, render, render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext
from shop.models import *

class ProductAddForm(ModelForm):
    # Auto generated form to create Product model.
    class Meta:
        model = Product
        exclude = ('user','enabled','expiration','sold',)

def index(request):
    title = 'Shop'
    if 'q' in request.GET:
        products = Product.objects.filter(title__icontains=request.GET['q'])
        variables = RequestContext(request, {
            'title': title,
            'search': 'You searched for: %r' % request.GET['q'],
            # 'products': get_list_or_404(Product, title__icontains=request.GET['q']),
            'products': products,
            # 'condition': product_condition.get_condition_display(),
        })
        # print variables.condition
    else:
        variables = RequestContext(request, {
            'title': title,
            'category': Category.objects.all(),
        })
    return render(request, 'shop/index.html', variables)

def category(request, **kwargs):
    if 'pcategory' in kwargs:
        variables = RequestContext(request, {
            'title': '%s - %s' % (kwargs['pcategory'], kwargs['category']),
            'pcategory': kwargs['pcategory'],
            'category': kwargs['category'],
            'products': get_list_or_404(Product.objects.filter(category__pid__name=kwargs['pcategory']), category__name=kwargs['category']),
        })
    else:
        variables = RequestContext(request, {
            'title': kwargs['category'],
            'category': kwargs['category'],
            'products': get_list_or_404(Product, category__pid__name=kwargs['category']),
            # 'products': get_list_or_404(Product, category__name=kwargs['category']),
        })
    return render(request, 'shop/category.html', variables)

def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    title = product.title
    try:
        print WatchList.objects.get(product=product, user=request.user)
        watch = 'Ignore'
        pass
    except ObjectDoesNotExist:
        watch = 'Watch'
        pass
    variables = RequestContext(request, {
        'title': title,
        'product': product,
        'condition': product.get_condition_display(),
        'shiptype': product.get_shiptype_display(),
        'watch': watch,
    })
    return render(request, 'shop/product.html', variables)

def product_add(request):
    title = 'Add Product'
    if request.method == 'POST':
        form = ProductAddForm(request.POST)
        if form.is_valid():
            # Create a new Server object.
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('/shop/%s/' % new_product.id)
    else:
        form = ProductAddForm()

    variables = RequestContext(request, {
        'title': title,
        'form': form,
    })
    return render_to_response('shop/product_add.html', variables)

def product_buy(request, **kwargs):
    title = 'Buy Product'
    variables = RequestContext(request, {
        'title': title,
        'product': get_object_or_404(Product, id=kwargs['product_id']),
    })
    return render_to_response('shop/product_buy.html', variables)

def watch(request, **kwargs):
    print 'kwargs: %s' % kwargs
    if request.user.is_active:
        if 'product_id' in kwargs:
            if 'ignore' in kwargs:
                WatchList.objects.get(product=kwargs['product_id'], user=request.user.id).delete()
                return redirect('/shop/watch/')
            if 'add' in kwargs:
                product = get_object_or_404(Product, id=kwargs['product_id'])
                watch = WatchList(product=product, user=request.user)
                watch.save()
                return redirect('/shop/watch/')
        watches = WatchList.objects.filter(user_id=request.user.id)
    else:
        watches = Nothing
    title = 'Watch List'
    variables = RequestContext(request, {
        'title': title,
        'watches': watches,
    })
    return render(request, 'shop/watch.html', variables)

def watch_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_active:
        watch = WatchList(product=product, user=request.user)
        watch.save()
    return redirect('/shop/%s/' % product_id)

def watch_ignore(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_active:
        WatchList.objects.get(product=product_id, user=request.user.id).delete()
    return redirect('/shop/%s/' % product_id)
