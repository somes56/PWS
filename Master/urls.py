from django.urls import path, include
from Master import views

urlpatterns = [
    path('CustomerList', views.CustomerList, name='CustomerList'),
    path('PartialCustomerList', views.PartialCustomerList, name='PartialCustomerList'),
    path('PartialCustomerList/<str:SearchBy>/', views.PartialCustomerList, name='PartialCustomerList'),
    path('CustomerForm', views.CustomerForm, name='CustomerForm'),
    path('CustomerForm/<uuid:CustomerID>/', views.CustomerForm, name='CustomerForm'),
    path('DeleteCustomer/<uuid:CustomerID>/', views.DeleteCustomer, name='DeleteCustomer'),
    
    path('PortList', views.PortList, name='PortList'),
    path('PartialPortList', views.PartialPortList, name='PartialPortList'),
    path('PartialPortList/<str:SearchBy>/', views.PartialPortList, name='PartialPortList'),
    path('PortForm', views.PortForm, name='PortForm'),
    path('PortForm/<uuid:PortID>/', views.PortForm, name='PortForm'),
    path('DeletePort/<uuid:PortID>/', views.DeletePort, name='DeletePort'),

    path('UpsertCountry', views.UpsertCountry, name='UpsertCountry')
]