from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_std', views.all_std, name='all_std'),
    path('add_std', views.add_std, name='add_std'),
    path('remove_std', views.remove_std, name='remove_std'),
    path('remove_std/<int:std_id>', views.remove_std, name='remove_std'),
    path('filter_std', views.filter_std, name='filter_std'),
]