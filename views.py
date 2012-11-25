from django.shortcuts import render, get_list_or_404, get_object_or_404

def index(request):
    return render(request, 'index.html')

def account_index(request):
    return render(request, 'registration/index.html')