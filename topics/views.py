from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import topic


def index(request, subject, subtopic, slug):
    subject = subject
    subtopic = subtopic
    slug = slug
    pg = topic.objects.get(slug=slug)
    context = {
        'topic':pg.topic_text,
        'content':pg.content,
        'related':pg.related,
        'description':pg.description,
    }
    return render(request, 'topics/topic.html', context)

def subject_view(request, subject):
    subject = subject
    pg = topic.objects.get(subject=subject)
    context = {
        'topic':pg.topic_text,
        'content':pg.content,
        'related':pg.related,
        'description':pg.description,
    }
    return render(request, 'papermasters/subject.html', context)

def topic_view(request):
    topic_objects = topic.objects.all()[:5]
    return render(request, 'papermasters/topic.html', {'topic_objects':topic_objects})


