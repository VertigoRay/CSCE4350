from django.conf.urls import patterns, url
from shop import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.product_add, name='product_add'),
    url(r'^watch/$', views.watch, name='watch'),
    url(r'^watch/(?P<product_id>\d+)/(?P<ignore>ignore)/$', views.watch, name='watch_prod_ignore'),
    url(r'^watch/(?P<product_id>\d+)/(?P<add>add)/$', views.watch, name='watch_prod_ignore'),
    url(r'^(?P<product_id>\d+)/$', views.product, name='product'),
    url(r'^(?P<product_id>\d+)/buy/$', views.product_buy, name='product_buy'),
    url(r'^(?P<product_id>\d+)/watch/$', views.watch_add, name='watch_add'),
    url(r'^(?P<product_id>\d+)/ignore/$', views.watch_ignore, name='watch_ignore'),
    url(r'^(?P<category>\w+)/$', views.category, name='category'),
    url(r'^(?P<pcategory>\w+)/(?P<category>\w+)/$', views.category, name='pcategory'),
)