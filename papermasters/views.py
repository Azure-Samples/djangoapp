from pydoc_data.topics import topics
from django.forms import SlugField
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import topic

def topic_view(request):
    return render(request, 'papermasters/topic.html')

