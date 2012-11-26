from django.contrib.auth.models import User
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template import Context, loader
from profile.models import *

def index(request):
    user_list = get_list_or_404(User.objects.order_by('name'))
    return render(request, 'profile/index.html', {'user_list': user_list})

def detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile/detail.html', {'user': user})