from django.urls import path
from . import views

app_name='topics'

urlpatterns = [
    path('', views.index, {'slug':''}, name='home'),
    path('<slug:slug>', views.subject_view, name= 'subject_view'),
    path('<str:subject>/<slug:slug>', views.subtopic_view, name= 'subtopic_view'),
    path('<str:subject>/<str:subtopic>/<slug:slug>', views.index, name= 'index'),
]