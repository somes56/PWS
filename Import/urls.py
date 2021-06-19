from django.urls import path, include
from Import import views

urlpatterns = [
    path("OblList", views.OblList, name="OblList"),
    path("PartialOblList", views.PartialOblList, name="PartialOblList"),
    path(
        "PartialOblList/<str:SearchBy>/",
        views.PartialOblList,
        name="PartialOblList",
    ),
    path("OblForm", views.OblForm, name="OblForm"),
    path("OblForm/<uuid:OblID>/", views.OblForm, name="OblForm"),
    path("DeleteObl/<uuid:OblID>/", views.DeleteObl, name="DeleteObl"),
    path("ContainerList", views.ContainerList, name="ContainerList"),
    path(
        "PartialContainerList", views.PartialContainerList, name="PartialContainerList"
    ),
    path(
        "PartialContainerList/<str:SearchBy>/",
        views.PartialContainerList,
        name="PartialContainerList",
    ),
    path("ContainerForm", views.ContainerForm, name="ContainerForm"),
    path(
        "ContainerForm/<uuid:ContainerID>/", views.ContainerForm, name="ContainerForm"
    ),
    path(
        "DeleteContainer/<uuid:ContainerID>/",
        views.DeleteContainer,
        name="DeleteContainer",
    ),
    path("HblList", views.HblList, name="HblList"),
    path("PartialHblList", views.PartialHblList, name="PartialHblList"),
    path(
        "PartialHblList/<str:SearchBy>/",
        views.PartialHblList,
        name="PartialHblList",
    ),
    path("HblForm", views.HblForm, name="HblForm"),
    path("HblForm/<uuid:HblID>/", views.HblForm, name="HblForm"),
    path(
        "DeleteHbl/<uuid:HblID>/",
        views.DeleteHbl,
        name="DeleteHbl",
    ),
    path(
        "UnstuffContainerList", views.UnstuffContainerList, name="UnstuffContainerList"
    ),
    path(
        "PartialUnstuffContainerPendingList",
        views.PartialUnstuffContainerPendingList,
        name="PartialUnstuffContainerPendingList",
    ),
    path(
        "PartialUnstuffContainerPendingList/<str:SearchBy>/",
        views.PartialUnstuffContainerPendingList,
        name="PartialUnstuffContainerPendingList",
    ),
    path(
        "PartialUnstuffContainerCompletedList",
        views.PartialUnstuffContainerCompletedList,
        name="PartialUnstuffContainerCompletedList",
    ),
    path(
        "PartialUnstuffContainerCompletedList/<str:SearchBy>/",
        views.PartialUnstuffContainerCompletedList,
        name="PartialUnstuffContainerCompletedList",
    ),
    path(
        "UnstuffContainerForm/<uuid:ContainerID>/",
        views.UnstuffContainerForm,
        name="UnstuffContainerForm",
    ),
    path("InvoiceList", views.InvoiceList, name="InvoiceList"),
    path("PartialInvoiceList", views.PartialInvoiceList, name="PartialInvoiceList"),
    path(
        "PartialInvoiceList/<str:SearchBy>/",
        views.PartialInvoiceList,
        name="PartialInvoiceList",
    ),
    path(
        "PartialInvoiceItemList",
        views.PartialInvoiceItemList,
        name="PartialInvoiceItemList",
    ),
    path(
        "PartialInvoiceItemList/<uuid:InvoiceID>/",
        views.PartialInvoiceItemList,
        name="PartialInvoiceItemList",
    ),
    path("InvoiceForm", views.InvoiceForm, name="InvoiceForm"),
    path("InvoiceForm/<uuid:InvoiceID>/", views.InvoiceForm, name="InvoiceForm"),
    path(
        "DeleteInvoice/<uuid:InvoiceID>/<str:DeleteRemark>",
        views.DeleteInvoice,
        name="DeleteInvoice",
    ),
    path(
        "UpsertInvoiceItem/<uuid:InvoiceID>/<uuid:ItemID>/<int:ItemQuantity>/<str:ItemUnitAmount>/",
        views.UpsertInvoiceItem,
        name="UpsertInvoiceItem",
    ),
    path(
        "UpsertInvoiceItem/<uuid:InvoiceID>/<uuid:InvoiceItemID>/<uuid:ItemID>/<int:ItemQuantity>/<str:ItemUnitAmount>/",
        views.UpsertInvoiceItem,
        name="UpsertInvoiceItem",
    ),
    path(
        "DeleteInvoiceItem/<uuid:InvoiceItemID>/",
        views.DeleteInvoiceItem,
        name="DeleteInvoiceItem",
    ),
    path(
        "UpsertDefaultInvoiceItem/<uuid:InvoiceID>/",
        views.UpsertDefaultInvoiceItem,
        name="UpsertDefaultInvoiceItem",
    ),
    path("CreditList", views.CreditList, name="CreditList"),
    path("PartialCreditList", views.PartialCreditList, name="PartialCreditList"),
    path(
        "PartialCreditList/<str:SearchBy>/",
        views.PartialCreditList,
        name="PartialCreditList",
    ),
    path(
        "PartialCreditItemList",
        views.PartialCreditItemList,
        name="PartialCreditItemList",
    ),
    path(
        "PartialCreditItemList/<uuid:CreditID>/",
        views.PartialCreditItemList,
        name="PartialCreditItemList",
    ),
    path("CreditForm", views.CreditForm, name="CreditForm"),
    path("CreditForm/<uuid:CreditID>/", views.CreditForm, name="CreditForm"),
    path(
        "UpsertCreditItem/<uuid:CreditID>/<uuid:ItemID>/<int:ItemQuantity>/<str:ItemUnitAmount>/<int:IsDefaultItem>/",
        views.UpsertCreditItem,
        name="UpsertCreditItem",
    ),
    path(
        "UpsertCreditItem/<uuid:CreditID>/<uuid:CreditItemID>/<uuid:ItemID>/<int:ItemQuantity>/<str:ItemUnitAmount>/<int:IsDefaultItem>/",
        views.UpsertCreditItem,
        name="UpsertCreditItem",
    ),
    path(
        "DeleteCredit/<uuid:CreditID>/<str:DeleteRemark>",
        views.DeleteCredit,
        name="DeleteCredit",
    ),
    path(
        "DeleteCreditItem/<uuid:CreditItemID>/",
        views.DeleteCreditItem,
        name="DeleteCreditItem",
    ),
]
