
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import topic


def index(request):
    return render(request, 'papermasters/index.html')

def topic_view(request):
    topic_objects = topic.objects.all()[:5]
    return render(request, 'papermasters/topic.html', {'topic_objects':topic_objects})




