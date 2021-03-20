from django.urls import path, include
from Master import views

urlpatterns = [
    path("CustomerList", views.CustomerList, name="CustomerList"),
    path("PartialCustomerList", views.PartialCustomerList, name="PartialCustomerList"),
    path(
        "PartialCustomerList/<str:SearchBy>/",
        views.PartialCustomerList,
        name="PartialCustomerList",
    ),
    path("CustomerForm", views.CustomerForm, name="CustomerForm"),
    path("CustomerForm/<uuid:CustomerID>/", views.CustomerForm, name="CustomerForm"),
    path(
        "DeleteCustomer/<uuid:CustomerID>/", views.DeleteCustomer, name="DeleteCustomer"
    ),
    path("PortList", views.PortList, name="PortList"),
    path("PartialPortList", views.PartialPortList, name="PartialPortList"),
    path(
        "PartialPortList/<str:SearchBy>/", views.PartialPortList, name="PartialPortList"
    ),
    path("PortForm", views.PortForm, name="PortForm"),
    path("PortForm/<uuid:PortID>/", views.PortForm, name="PortForm"),
    path("DeletePort/<uuid:PortID>/", views.DeletePort, name="DeletePort"),
    path("UnitList", views.UnitList, name="UnitList"),
    path("PartialUnitList", views.PartialUnitList, name="PartialUnitList"),
    path(
        "PartialUnitList/<str:SearchBy>/", views.PartialUnitList, name="PartialUnitList"
    ),
    path("UnitForm", views.UnitForm, name="UnitForm"),
    path("UnitForm/<uuid:UnitID>/", views.UnitForm, name="UnitForm"),
    path("DeleteUnit/<uuid:UnitID>/", views.DeleteUnit, name="DeleteUnit"),
    path("ContainerSizeList", views.ContainerSizeList, name="ContainerSizeList"),
    path(
        "PartialContainerSizeList",
        views.PartialContainerSizeList,
        name="PartialContainerSizeList",
    ),
    path(
        "PartialContainerSizeList/<str:SearchBy>/",
        views.PartialContainerSizeList,
        name="PartialContainerSizeList",
    ),
    path("ContainerSizeForm", views.ContainerSizeForm, name="ContainerSizeForm"),
    path(
        "ContainerSizeForm/<uuid:ContainerSizeID>/",
        views.ContainerSizeForm,
        name="ContainerSizeForm",
    ),
    path(
        "DeleteContainerSize/<uuid:ContainerSizeID>/",
        views.DeleteContainerSize,
        name="DeleteContainerSize",
    ),
    path("VesselList", views.VesselList, name="VesselList"),
    path("PartialVesselList", views.PartialVesselList, name="PartialVesselList"),
    path(
        "PartialVesselList/<str:SearchBy>/",
        views.PartialVesselList,
        name="PartialVesselList",
    ),
    path("VesselForm", views.VesselForm, name="VesselForm"),
    path("VesselForm/<uuid:VesselID>/", views.VesselForm, name="VesselForm"),
    path("DeleteVessel/<uuid:VesselID>/", views.DeleteVessel, name="DeleteVessel"),
    path("ItemList", views.ItemList, name="ItemList"),
    path("PartialItemList", views.PartialItemList, name="PartialItemList"),
    path(
        "PartialItemList/<str:SearchBy>/", views.PartialItemList, name="PartialItemList"
    ),
    path("ItemForm", views.ItemForm, name="ItemForm"),
    path("ItemForm/<uuid:ItemID>/", views.ItemForm, name="ItemForm"),
    path("DeleteItem/<uuid:ItemID>/", views.DeleteItem, name="DeleteItem"),
    path("ClassList", views.ClassList, name="ClassList"),
    path("PartialClassList", views.PartialClassList, name="PartialClassList"),
    path(
        "PartialClassList/<str:SearchBy>/",
        views.PartialClassList,
        name="PartialClassList",
    ),
    path("ClassForm", views.ClassForm, name="ClassForm"),
    path("ClassForm/<uuid:ClassID>/", views.ClassForm, name="ClassForm"),
    path("DeleteClass/<uuid:ClassID>/", views.DeleteClass, name="DeleteClass"),
    path("VoyageList", views.VoyageList, name="VoyageList"),
    path("PartialVoyageList", views.PartialVoyageList, name="PartialVoyageList"),
    path(
        "PartialVoyageList/<str:SearchBy>/",
        views.PartialVoyageList,
        name="PartialVoyageList",
    ),
    path("VoyageForm", views.VoyageForm, name="VoyageForm"),
    path("VoyageForm/<uuid:VoyageID>/", views.VoyageForm, name="VoyageForm"),
    path("DeleteVoyage/<uuid:VoyageID>/", views.DeleteVoyage, name="DeleteVoyage"),
    path("OperatorList", views.OperatorList, name="OperatorList"),
    path("PartialOperatorList", views.PartialOperatorList, name="PartialOperatorList"),
    path(
        "PartialOperatorList/<str:SearchBy>/",
        views.PartialOperatorList,
        name="PartialOperatorList",
    ),
    path("OperatorForm", views.OperatorForm, name="OperatorForm"),
    path("OperatorForm/<uuid:OperatorID>/", views.OperatorForm, name="OperatorForm"),
    path(
        "DeleteOperator/<uuid:OperatorID>/", views.DeleteOperator, name="DeleteOperator"
    ),
    path("UpsertCountry", views.UpsertCountry, name="UpsertCountry"),
]