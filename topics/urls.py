from django.urls import path
from . import views

app_name='topics'

urlpatterns = [
    path('', views.TopicListView.as_view(), name='topic_changelist'),
    path('add/', views.TopicCreateView.as_view(), name='topic_add'),
    path('<int:pk>/', views.TopicUpdateView.as_view(), name='topic_change'),
    path('ajax/load-subtopics/', views.load_subtopics, name='ajax_load_subtopics'),  
    path('<slug:slug>', views.subject_view, name= 'subject_view'),
    path('<str:subject>/<slug:slug>', views.subtopic_view, name= 'subtopic_view'),
    path('<str:subject>/<str:subtopic>/<slug:slug>', views.index, name= 'index'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]