from shop.models import *
from django.contrib import admin

# class ComputerAdmin(admin.ModelAdmin):
#     readonly_fields = ('pub_date',)
#     fieldsets = [
#         (None,               {'fields': ['name','guid']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     list_display = ('name', 'guid', 'pub_date', 'was_published_today')

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name')

admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(Billing)
admin.site.register(Category)#, CategoryAdmin)
admin.site.register(Order)
admin.site.register(Product)