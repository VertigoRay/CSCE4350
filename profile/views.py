from django.contrib.auth.models import User
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template import Context, loader
from profile.models import *

def index(request):
    latest_user_list = User.objects.order_by('-date_joined')[:5]
    return render(request, 'profile/index.html', {'latest_user_list': latest_user_list})

def detail(request, username):
    user = get_object_or_404(username=username)
    return render(request, 'profile/detail.html', {'user': user})