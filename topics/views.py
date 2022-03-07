from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import topic


def topic_view(request):
    topic_objects = topic.objects.all()[:5]
    return render(request, 'topics/topic.html', {'topic_objects':topic_objects})
