from django.urls import path

from h import views

urlpatterns = [
    path('', views.home)
]