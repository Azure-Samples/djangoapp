from django.urls import path
from . import views

app_name='papermasters'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('', views.topic_view, name= 'topic_view'),
    path('papermasters/<int:id>/', views.detail_topic, name= 'detail_topic'),
]
