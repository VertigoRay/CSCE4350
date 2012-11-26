from django.conf.urls import patterns, url
from shop import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_id>\d+)/$', views.product),
    url(r'^(?P<category>\w+)/$', views.category),
    url(r'^productadd/$', views.product_add, name='index'),
)