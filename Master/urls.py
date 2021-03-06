from django.urls import path, include
from Master import views

urlpatterns = [
    path('Customer', views.Customer, name='Customer'),
    path('UpsertMstCountry', views.UpsertMstCountry, name='UpsertMstCountry')
]