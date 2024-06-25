from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  add_category, add_menu_item, menu_items, order_successful, index, log, signup, logout, supervisor, supervisorlogout, orders_table, users_table, back, dashboard, add_phone_number, create_blog, blogs, blog_list, edit_blog, delete_blog


urlpatterns = [
    path('', index, name='index'),
    path('log', log, name='log'),
    path('add_phone_number', add_phone_number, name='add_phone_number'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
    path('supervisorlogout', supervisorlogout, name='supervisorlogout'),
    path('supervisor', supervisor, name='supervisor'),
    path('orders_table', orders_table, name="orders_table"),
    path('users_table', users_table, name='users_table'),
    path('back', back, name='back'),
    path('dashboard', dashboard, name='dashboard'),
    path('add_category/', add_category, name='add_category'),
    path('add_menu_item/', add_menu_item, name='add_menu_item'),
    path('menu_items/', menu_items, name='menu_items'),
    path('order_successful/', order_successful, name='order_successful'),  # Updated from place_order
    path('create_blog', create_blog, name='create_blog'),
    path('blogs', blogs, name='blogs'),
    path('blog_list', blog_list, name='blog_list'),
    path('edit_blog/<int:blog_id>/', edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>/', delete_blog, name='delete_blog'),
]
