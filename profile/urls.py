from django.conf.urls import patterns, url
from profile import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>\w+)/$', views.detail, name='detail'),
    url(r'^(?P<username>\w+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<username>\w+)/orders/$', views.orders, name='orders'),
    url(r'^(?P<username>\w+)/products/$', views.products, name='products'),
    url(r'^(?P<username>\w+)/rate/$', views.rate, name='rate'),
    url(r'^(?P<username>\w+)/rating/$', views.rating, name='rating'),
)