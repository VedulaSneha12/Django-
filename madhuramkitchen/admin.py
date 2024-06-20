from django.contrib import admin
from .models import Category, Order, OrderItem, MenuItem
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # Customize the admin options here if necessary
    pass

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')
admin.site.register(User, UserAdmin)