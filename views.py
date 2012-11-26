from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template import RequestContext

def index(request):
    variables = RequestContext(request, {
        'title':    'Home',
    })
    return render(request, 'index.html', variables)

def account_index(request):
    return render(request, 'registration/index.html')