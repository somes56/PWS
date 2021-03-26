from django.urls import path, include
from Import import views

urlpatterns = [path("OblList", views.OblList, name="OblList")]
