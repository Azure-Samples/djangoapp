
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import topic


def index(request, slug):
    slug = slug
    pg = topic.objects.get(slug=slug)
    context = {
        'topic':pg.topic_text,
        'content':pg.content,
        'related':pg.related,
    }
    return render(request, 'papermasters/topic.html', context)

def topic_view(request):
    topic_objects = topic.objects.all()[:5]
    return render(request, 'papermasters/topic.html', {'topic_objects':topic_objects})




