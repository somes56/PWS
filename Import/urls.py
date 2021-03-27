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
]
