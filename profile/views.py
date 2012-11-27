from django.contrib.auth.models import User, UserProfile
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
    variables = RequestContext(request, {
        'title': username,
        'user_profile':	get_object_or_404(User, username=username),
        #'user_phone': get_object_or_404(UserProfile, username=phone),
    })
    return render(request, 'profile/detail.html', variables)