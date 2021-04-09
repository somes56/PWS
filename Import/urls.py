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
    path("UnstuffContainerForm/<uuid:ContainerID>/", views.UnstuffContainerForm, name="UnstuffContainerForm"),
]
