from django.forms import ModelForm
from django.shortcuts import render, render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext
from shop.models import *

class ProductAddForm(ModelForm):
    # Auto generated form to create Product model.
    class Meta:
        model = Product

def index(request):
    return render(request, 'shop/index.html')

def product_add(request):
    """
    Create a new Server model.
    """
    if request.method == 'POST':
        form = ProductAddForm(request.POST)
        if form.is_valid():
            # Create a new Server object.
            form.save()
    else:
        form = ProductAddForm()
 
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response('shop/product_add.html', variables)