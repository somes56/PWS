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
]