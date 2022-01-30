from django.shortcuts import render
from django.http import HttpResponse
from .models import topic


def topic_view(request):
    return render(request, 'papermasters/topic.html')

