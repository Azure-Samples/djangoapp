from django.urls import path
from . import views

app_name='papermasters'

urlpatterns = [
    path('', views.index, {'topdetails':''}, name='home'),
    #path('', views.topic_view, name= 'topic_view'),
    path('<str:topdetails>', views.index, name= 'index'),
]
