from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import topic, subject


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

def subject_view(request, slug):
    slug = slug
    sg = subject.objects.get(slug=slug)
    context = {
        'subject':sg.subject_text,
        'meta_title':sg.meta_title,
        'content_two':sg.content_two,
        'content':sg.content,
        'description':sg.meta_description,
    }
    return render(request, 'topics/subject.html', context)

def topic_view(request):
    topic_objects = topic.objects.all()[:5]
    return render(request, 'topics/topic.html', {'topic_objects':topic_objects})


