from django.contrib.auth.models import User
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template import Context, loader, RequestContext
from profile.models import *

def index(request):
    variables = RequestContext(request, {
        'title':    'Profiles',
        'user_list':  get_list_or_404(User.objects.order_by('username')),
    })
    return render(request, 'profile/index.html', variables)

def detail(request, username):
    user_profile = get_object_or_404(User, username=username)
    user_profile_billing = get_object_or_404(Billing, user_id=user_profile.id)
    user_profile_address = get_object_or_404(Address, user_id=user_profile.id)[0]
    variables = RequestContext(request, {
        'title': username,
        'user_profile': user_profile,
        'user_profile_billing': user_profile_billing,
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
        'title': username,
        'user_profile': get_object_or_404(User, username=username),
    })
    return render(request, 'profile/orders.html', variables)

def products(request, username):
    variables = RequestContext(request, {
        'title': username,
        'user_profile':	get_object_or_404(User, username=username),
    })
    return render(request, 'profile/products.html', variables)