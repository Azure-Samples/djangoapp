from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import topic


def index(request, slug):
    
    slug = slug
    pg = topic.objects.get(slug=slug)
    context = {
        'topic':pg.topic_text,
        'meta_title':pg.meta_title,
        'content':pg.content,
        'related':pg.related,
        'description':pg.description,
    }
    return render(request, 'topics/topic.html', context)


def topic_view(request):
    topic_objects = topic.objects.all()[:5]
    return render(request, 'topics/topic.html', {'topic_objects':topic_objects})# Create your views here.
