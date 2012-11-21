from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>CSCE4350</h1><h2>Shop</h2>")