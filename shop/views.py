from django.shortcuts import render, get_list_or_404, get_object_or_404

def index(request):
    return render(request, 'shop/index.html')