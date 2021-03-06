from django.urls import path, include
from Master import views

urlpatterns = [
    path('Customer', views.Customer, name='Customer'),
    path('CustomerForm', views.CustomerForm, name='CustomerForm'),
    path('UpsertCountry', views.UpsertCountry, name='UpsertCountry')
]