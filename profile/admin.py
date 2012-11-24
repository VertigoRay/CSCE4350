from django.contrib import admin
from profile.models import *

class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,           {'fields': ['user']}),
        ('User Profile', {'fields': ['phone']}),
    ]

class AddressAdmin(admin.ModelAdmin):
    ordering = ['-pub_date']
    readonly_fields = ('pub_date',)

class BillingAdmin(admin.ModelAdmin):
    ordering = ['-pub_date']
    readonly_fields = ('pub_date',)

class RatingAdmin(admin.ModelAdmin):
    ordering = ['-pub_date']
    readonly_fields = ('pub_date',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Billing, BillingAdmin)
admin.site.register(Rating, RatingAdmin)