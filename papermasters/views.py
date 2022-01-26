from django.shortcuts import render
from django.http import HttpResponse


def topic(request):
    return render(request, 'papermasters/topic.html')