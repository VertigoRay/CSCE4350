from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='index'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^account/$', 'views.account_index', name='account_index'),
    url(r'^account/', include('registration.backends.default.urls')),

    url(r'^profile/', include('profile.urls', namespace='profile')),
    url(r'^shop/', include('shop.urls', namespace='shop')),
)
