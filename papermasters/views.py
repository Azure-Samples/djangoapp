from pydoc_data.topics import topics
from django.forms import SlugField
from django.shortcuts import render, get_object_or_404
from .models import topic


def topic_view(request, subject, subtopic, slug):
    topic_object = get_object_or_404(topic, slug=slug)
    return render(request, 'papermasters/topic.html',{'topic_object':topic})
