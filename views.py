from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>CSCE4350</h1><ul><li><a href="/admin">admin</a></li><li><a href="/profile">profile</a></li><li><a href="/shop">shop</a></li></ul>')