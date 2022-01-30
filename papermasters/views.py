from django.shortcuts import render
from django.http import HttpResponse
from .models import topic


def topic_view(request, subject, subtopic, slug):
    return render(request, 'papermasters/topic.html')

