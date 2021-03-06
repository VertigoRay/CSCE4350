from django.contrib.auth.models import User
from django.forms import ModelForm
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.template import Context, loader, RequestContext
from profile.models import *
from shop.models import *

class RateForm(ModelForm):
    # Auto generated form to create Product model.
    class Meta:
        model = Rating
        exclude = ('buyer','seller',)

def index(request):
    title = 'Profile'
    if not (request.user.is_staff):
        if request.user.is_active:
            return redirect('/profile/%s' % request.user.username)
        else:
            return redirect('/')
    variables = RequestContext(request, {
        'title':    title,
        'user_list':  get_list_or_404(User.objects.order_by('username')),
    })
    return render(request, 'profile/index.html', variables)

def detail(request, username):
    user_profile = get_object_or_404(User, username=username)
    user_profile_billing = Billing.objects.get(user_id=user_profile.id)
    user_profile_address = Address.objects.get(user_id=user_profile.id)
    
    rating = Rating.objects.filter(seller=user_profile.id).values('rating')
    rating_sum = int(sum(r['rating'] for r in rating))
    rating_count = int(len(rating))
    rating_avg = rating_sum/rating_count

    variables = RequestContext(request, {
        'title': username,
        'user_profile': user_profile,
        'user_profile_billing': user_profile_billing,
        'user_profile_address': user_profile_address,
        'rating_avg': rating_avg,
        'rating_count': rating_count,
    })
    return render(request, 'profile/detail.html', variables)

def edit(request, username):
    title = 'Edit Profile'
    variables = RequestContext(request, {
        'title': title,
        'user_profile': get_object_or_404(User, username=username),
    })
    return render(request, 'profile/edit.html', variables)

def orders(request, username):
    title = 'Order History'
    variables = RequestContext(request, {
        'title': title,
        'user_profile': get_object_or_404(User, username=username),
        'orders': Order.objects.filter(user__username=username).order_by('-id'),
    })
    return render(request, 'profile/orders.html', variables)

def products(request, username):
    title = 'My Products'
    variables = RequestContext(request, {
        'title': title,
        'user_profile': get_object_or_404(User, username=username),
        'products': Product.objects.filter(user__username=username).order_by('-pub_date'),
        'orders': Order.objects.filter(product__user__username=username).order_by('-id'),
    })
    return render(request, 'profile/products.html', variables)

def rate(request, username):
    title = 'Rate'
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            # Create a new Server object.
            new_rate = form.save(commit=False)
            new_rate.buyer = request.user
            new_rate.seller = get_object_or_404(User, username=username)
            new_rate.save()
            return redirect('/profile/%s/orders/' % request.user.username)
    else:
        form = RateForm()

    variables = RequestContext(request, {
        'title': title,
        'user_profile': get_object_or_404(User, username=username),
        'form': form,
    })
    return render(request, 'profile/rate.html', variables)

def rating(request, username):
    title = 'Rating'

    user_profile = get_object_or_404(User, username=username)
    
    rating = Rating.objects.filter(seller=user_profile.id).values('rating')
    rating_sum = int(sum(r['rating'] for r in rating))
    rating_count = int(len(rating))
    rating_avg = rating_sum/rating_count

    variables = RequestContext(request, {
        'title': title,
        'ratings':	get_list_or_404(Rating, seller=user_profile),
        'rating_avg': rating_avg,
        'rating_count': rating_count,
    })
    return render(request, 'profile/rating.html', variables)