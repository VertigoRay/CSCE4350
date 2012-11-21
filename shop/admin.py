from datetime import datetime, timedelta
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from shop.models import *
from profile.models import *

class Published(SimpleListFilter):
    # Human-readable title which will be displayed in the right admin sidebar just above the filter options.
    title = _('published')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'pub'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('day', _('published last day')),
            ('week', _('published last week')),
            ('month', _('published last month')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == 'day':
            return queryset.filter(pub_date__gte=timezone.now() - timedelta(days=1))
        if self.value() == 'week':
            return queryset.filter(pub_date__gte=timezone.now() - timedelta(days=7))
        if self.value() == 'month':
            return queryset.filter(pub_date__gte=timezone.now() - timedelta(days=30))


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pid', 'name')
    list_display_links = ('name',)
    list_filter = ('pid',)
    ordering = ['pid', 'name']

class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    ordering = ['-pub_date']
    readonly_fields = ('pub_date',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'pub_date', 'enabled')
    list_filter = ('enabled', Published,)
    date_hierarchy = 'pub_date'
    ordering = ['-pub_date']
    readonly_fields = ('pub_date','order',)
    fieldsets = [
        (None,                  {'fields': ['user','category','enabled']}),
        ('Product Details',     {'fields': ['title', 'desc', 'price', 'condition']}),
        ('Shipping Details',    {'fields': ['shiptype', 'shipfee']}),
        ('Date information',    {'fields': ['pub_date', 'expiration', 'sold'], 'classes': ['collapse']}),
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)