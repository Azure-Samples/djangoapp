from pydoc_data.topics import topics
from django.forms import SlugField
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import topic

def topic(request):
    return render(request, 'papermasters/topic.html')

def topic_view(request, slug):
    t = get_object_or_404(topic,slug=slug)
    return render(request, 'papermasters/topic.html',{'t':topic})
