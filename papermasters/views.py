from django.shortcuts import render
from django.http import HttpResponse


def topic(request, slug):
    return render(request, 'papermasters/topic.html', {'slug':slug})