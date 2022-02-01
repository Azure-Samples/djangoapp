
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import topic


def topic_view(request):
    return render(request, 'papermasters/topic.html')

def index(request):
    return render(request, 'papermasters/topic.html')

def topic_view(request):
    topic_objects = topic.objects.all()[:5]
    return render(request, 'papermasters/topic.html', {'topic_objects':topic_objects})

def detail_topic(request, id):
    obj = topic.objects.get(id=id)
    context = {
        "object": obj
    }
    return render(request, 'papermasters/topic_details.html', context)


