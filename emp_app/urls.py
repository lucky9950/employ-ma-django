from django.contrib import admin
from django.urls import path
from emp_app import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('all_emp',views.view_all_emp, name = 'all_emp'),
    path('add_emp',views.add_emp, name = 'add_emp'),
    path('remove_emp',views.remove_emp, name = 'remove_emp'),
    path('filter_emp',views.filter_emp, name = 'filter_emp'),
]
