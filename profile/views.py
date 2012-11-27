from django.contrib.auth.models import User
from django.forms import ModelForm
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template import Context, loader, RequestContext
from profile.models import *
from shop.models import *

class RateForm(ModelForm):
    # Auto generated form to create Product model.
    class Meta:
        model = Rating
        exclude = ('seller','buyer',)

def index(request):
    variables = RequestContext(request, {
        'title':    'Profiles',
        'user_list':  get_list_or_404(User.objects.order_by('username')),
    })
    return render(request, 'profile/index.html', variables)

def detail(request, username):
    user_profile = get_object_or_404(User, username=username)
    user_profile_billing = Billing.objects.get(user_id=user_profile.id)
    user_profile_address = Address.objects.get(user_id=user_profile.id)
    variables = RequestContext(request, {
        'title': username,
        'user_profile': user_profile,
        'user_profile_billing': user_profile_billing,
        'user_profile_address': user_profile_address,
    })
    return render(request, 'profile/detail.html', variables)

def edit(request, username):
    variables = RequestContext(request, {
        'title': username,
        'user_profile': get_object_or_404(User, username=username),
    })
    return render(request, 'profile/edit.html', variables)

def orders(request, username):
    variables = RequestContext(request, {
        'title': 'Order History - %s' % username,
        'user_profile': get_object_or_404(User, username=username),
        'orders': Order.objects.filter(user__username=username).order_by('-id'),
    })
    return render(request, 'profile/orders.html', variables)

def products(request, username):
    variables = RequestContext(request, {
        'title': 'My Products - %s' % username,
        'user_profile': get_object_or_404(User, username=username),
        'products': Product.objects.filter(user__username=username).order_by('-pub_date'),
        'orders': Order.objects.filter(product__user__username=username).order_by('-id'),
    })
    return render(request, 'profile/products.html', variables)

def rate(request, username):
    if request.method == 'POST':
        seller = username
        buyer = 'cworley' # This needs to reference the current logged on user. Note:  'user.username' doesn't work.
        form = RateForm(request.POST)
        if form.is_valid():
            # Create a new Server object.
            form.save()
    else:
        form = RateForm()

    variables = RequestContext(request, {
        'title': 'Rate - %s' % username,
        'user_profile':	get_object_or_404(User, username=username),
        'form': form,
    })
    return render(request, 'profile/rate.html', variables)