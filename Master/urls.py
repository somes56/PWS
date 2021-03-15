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

    path('UnitList', views.UnitList, name='UnitList'),
    path('PartialUnitList', views.PartialUnitList, name='PartialUnitList'),
    path('PartialUnitList/<str:SearchBy>/', views.PartialUnitList, name='PartialUnitList'),
    path('UnitForm', views.UnitForm, name='UnitForm'),
    path('UnitForm/<uuid:UnitID>/', views.UnitForm, name='UnitForm'),
    path('DeleteUnit/<uuid:UnitID>/', views.DeleteUnit, name='DeleteUnit'),

    path('ContainerSizeList', views.ContainerSizeList, name='ContainerSizeList'),
    path('PartialContainerSizeList', views.PartialContainerSizeList, name='PartialContainerSizeList'),
    path('PartialContainerSizeList/<str:SearchBy>/', views.PartialContainerSizeList, name='PartialContainerSizeList'),
    path('ContainerSizeForm', views.ContainerSizeForm, name='ContainerSizeForm'),
    path('ContainerSizeForm/<uuid:ContainerSizeID>/', views.ContainerSizeForm, name='ContainerSizeForm'),
    path('DeleteContainerSize/<uuid:ContainerSizeID>/', views.DeleteContainerSize, name='DeleteContainerSize'),

    path('VesselList', views.VesselList, name='VesselList'),
    path('PartialVesselList', views.PartialVesselList, name='PartialVesselList'),
    path('PartialVesselList/<str:SearchBy>/', views.PartialVesselList, name='PartialVesselList'),
    path('VesselForm', views.VesselForm, name='VesselForm'),
    path('VesselForm/<uuid:VesselID>/', views.VesselForm, name='VesselForm'),
    path('DeleteVessel/<uuid:VesselID>/', views.DeleteVessel, name='DeleteVessel'),

    path('UpsertCountry', views.UpsertCountry, name='UpsertCountry')
]