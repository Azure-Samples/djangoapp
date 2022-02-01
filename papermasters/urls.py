from django.urls import path
from . import views

app_name='papermasters'

urlpatterns = [
    path('', views.topic_view, name= 'topic_view'),
    path('papermasters/<bigint:id>/', views.detail_topic, name= 'detail_topic'),
]
