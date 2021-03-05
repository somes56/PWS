from django.urls import path, include
from Login import views

urlpatterns = [
    path('', views.Login, name='Login'),
    path('Login', views.Login, name='Login')
]