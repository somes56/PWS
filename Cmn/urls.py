from django.urls import path, include
from Cmn import views

urlpatterns = [
    path("AdvSearchState", views.AdvSearchState, name="AdvSearchState"),
    path("AdvSearchState/<str:SearchBy>/", views.AdvSearchState, name="AdvSearchState"),
    path("AdvSearchCountry", views.AdvSearchCountry, name="AdvSearchCountry"),
    path(
        "AdvSearchCountry/<str:SearchBy>/",
        views.AdvSearchCountry,
        name="AdvSearchCountry",
    ),
    path("AdvSearchTerm", views.AdvSearchTerm, name="AdvSearchTerm"),
    path("AdvSearchTerm/<str:SearchBy>/", views.AdvSearchTerm, name="AdvSearchTerm"),
    path("AdvSearchCustomer", views.AdvSearchCustomer, name="AdvSearchCustomer"),
    path(
        "AdvSearchCustomer/<str:SearchBy>/",
        views.AdvSearchCustomer,
        name="AdvSearchCustomer",
    ),
    path("AdvSearchVessel", views.AdvSearchVessel, name="AdvSearchVessel"),
    path(
        "AdvSearchVessel/<str:SearchBy>/", views.AdvSearchVessel, name="AdvSearchVessel"
    ),
    path("AdvSearchVoyage", views.AdvSearchVoyage, name="AdvSearchVoyage"),
    path(
        "AdvSearchVoyage/<str:SearchBy>/", views.AdvSearchVoyage, name="AdvSearchVoyage"
    ),
    path("AdvSearchPort", views.AdvSearchPort, name="AdvSearchPort"),
    path("AdvSearchPort/<str:SearchBy>/", views.AdvSearchPort, name="AdvSearchPort"),
    path(
        "AdvSearchContainerSize",
        views.AdvSearchContainerSize,
        name="AdvSearchContainerSize",
    ),
    path(
        "AdvSearchContainerSize/<str:SearchBy>/",
        views.AdvSearchContainerSize,
        name="AdvSearchContainerSize",
    ),
    path("AdvSearchClass", views.AdvSearchClass, name="AdvSearchClass"),
    path("AdvSearchClass/<str:SearchBy>/", views.AdvSearchClass, name="AdvSearchClass"),
    path("AdvSearchUnit", views.AdvSearchUnit, name="AdvSearchUnit"),
    path("AdvSearchUnit/<str:SearchBy>/", views.AdvSearchUnit, name="AdvSearchUnit"),
    path("AdvSearchObl", views.AdvSearchObl, name="AdvSearchObl"),
    path("AdvSearchObl/<str:SearchBy>/", views.AdvSearchObl, name="AdvSearchObl"),
    path(
        "AdvSearchContainerByObl",
        views.AdvSearchContainerByObl,
        name="AdvSearchContainerByObl",
    ),
    path(
        "AdvSearchContainerByObl/<uuid:OblID>/",
        views.AdvSearchContainerByObl,
        name="AdvSearchContainerByObl",
    ),
    path(
        "AdvSearchContainerByObl/<uuid:OblID>/<str:SearchBy>/",
        views.AdvSearchContainerByObl,
        name="AdvSearchContainerByObl",
    ),
    path(
        "AdvSearchHblByContainer/<uuid:ContainerID>/",
        views.AdvSearchHblByContainer,
        name="AdvSearchHblByContainer",
    ),
    path(
        "AdvSearchHblByContainer/<uuid:ContainerID>/<str:SearchBy>/",
        views.AdvSearchHblByContainer,
        name="AdvSearchHblByContainer",
    ),
    path("AdvSearchHblHist", views.AdvSearchHblHist, name="AdvSearchHblHist"),
    path(
        "AdvSearchHblHist/<str:SearchBy>/",
        views.AdvSearchHblHist,
        name="AdvSearchHblHist",
    ),
    path("AdvSearchItem", views.AdvSearchItem, name="AdvSearchItem"),
    path("AdvSearchItem/<str:SearchBy>/", views.AdvSearchItem, name="AdvSearchItem"),
]