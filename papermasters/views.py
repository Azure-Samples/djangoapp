from pydoc_data.topics import topics
from django.forms import SlugField
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from papermasters.models import topic

def topic_view(request, subject, subtopic, slug):
    try:
        p = topic.objects.get(pk=id)
    except topic.DoesNotExist:
        raise Http404("Sorry, nothing here to see")
    return render(request, 'papermasters/topic.html',{'topic':p})
