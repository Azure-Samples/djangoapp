from django.urls import path
from .views import TopicDetailView
from . import views

urlpatterns = [
    path('.', views.index, name='index'),
    path('<slug:slug>', views.index, name='index'),
]