from django.urls import path, include
from Master import views

urlpatterns = [
    path('CustomerList', views.CustomerList, name='CustomerList'),
    path('PartialCustomerList', views.PartialCustomerList, name='PartialCustomerList'),
    path('PartialCustomerList/<str:SearchBy>/', views.PartialCustomerList, name='PartialCustomerList'),
    path('CustomerForm', views.CustomerForm, name='CustomerForm'),
    path('CustomerForm/<uuid:CustomerID>/', views.CustomerForm, name='CustomerForm'),
    path('DeleteCustomer/<uuid:CustomerID>/', views.DeleteCustomer, name='DeleteCustomer'),
    path('UpsertCountry', views.UpsertCountry, name='UpsertCountry')
]