from django.shortcuts import render
from django.http import HttpResponse


def topic(request, slug):
    return render(request, 'papermasters/templates/topic.html', {'slug':slug})