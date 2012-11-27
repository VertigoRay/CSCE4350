from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='index'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^account/$', 'views.account_index', name='account_index'),
    url(r'^account/', include('registration.backends.default.urls', namespace='account'), name='Account'),

    url(r'^profile/', include('profile.urls', namespace='profile'), name='Profile'),
    url(r'^shop/', include('shop.urls', namespace='shop'), name='Shop'),
)
