from pydoc_data.topics import topics
from django.forms import SlugField
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import topic

def topic_view(request):
    return render(request, 'papermasters/topic.html')

def topic_view(request):
    topic_objects = topic.objects.all()[:5]
    return render(request, 'papermasters/topic.html', {'topic_objects':topic_objects})

def detail(request, id):
    topic_details = get_object_or_404(topic, id=self.kwargs['slug'])
    return render(request, 'papermasters/topic-details.html',{'topic_detatils':topic_details})


