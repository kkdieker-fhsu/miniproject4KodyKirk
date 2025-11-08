from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("endpoints/", views.endpoints, name="endpoints"),

    path("traffic/", views.traffic, name="traffic"),

    path("detail/<str:ip_address>/", views.detail, name="detail"),


]
