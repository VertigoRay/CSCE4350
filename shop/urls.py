from django.conf.urls import patterns, url
from shop import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.product_add, name='add'),
    url(r'^(?P<product_id>\d+)/$', views.product, name='product'),
    url(r'^(?P<category>\w+)/$', views.category, name='category'),
)