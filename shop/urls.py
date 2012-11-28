from django.conf.urls import patterns, url
from shop import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.product_add, name='add'),
    url(r'^watch/$', views.watch, name='watch'),
    url(r'^(?P<product_id>\d+)/$', views.product, name='product'),
    url(r'^(?P<product_id>\d+)/watch/$', views.watch_add, name='watch_add'),
    url(r'^(?P<product_id>\d+)/ignore/$', views.watch_ignore, name='watch_ignore'),
    url(r'^(?P<category>\w+)/$', views.category, name='category'),
    url(r'^(?P<pcategory>\w+)/(?P<category>\w+)/$', views.category, name='pcategory'),
)