from django.urls import path

from . import views



urlpatterns = [

    path("cars/<int:pk>/", views.car_detail, name="car_detail"),

]