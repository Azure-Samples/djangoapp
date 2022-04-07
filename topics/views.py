from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import TopicForm
from .models import Topic, Subject, Subtopic


def index(request, subject, subtopic, slug):
    subject = subject
    subtopic = subtopic
    slug = slug
    pg = Topic.objects.get(slug=slug)
    context = {
        'topic':pg.name,
        'meta_title':pg.meta_title,
        'content':pg.content,
        'related':pg.related,
        'description':pg.meta_description,
    }
    return render(request, 'topics/topic.html', context)

def subject_view(request, slug):
    slug = slug
    sg = Subject.objects.get(slug=slug)
    context = {
        'subject':sg.name,
        'meta_title':sg.meta_title,
        'content_two':sg.content_two,
        'content':sg.content,
        'description':sg.meta_description,
    }
    return render(request, 'topics/subject.html', context)

def subtopic_view(request, subject, slug):
    subject = subject
    slug = slug
    spg = Subtopic.objects.get(slug=slug)
    context = {
        'subtopic':spg.name,
        'meta_title':spg.meta_title,
        'content_two':spg.content_two,
        'content':spg.content,
        'description':spg.meta_description,
    }
    return render(request, 'topics/subtopic.html', context)

def topic_view(request):
    topic_objects = Topic.objects.all()[:5]
    return render(request, 'topics/topic.html', {'topic_objects':topic_objects})

#Views for Dropdown list below

class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'

class TopicCreateView(CreateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy('topic_changelist')

class TopicUpdateView(UpdateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy('topic_changelist')

def load_subtopics(request):
    subject_id = request.GET.get('subject')
    subtopics = Subtopic.objects.filter(subject_id=subject_id).order_by('name')
    return render(request, 'subtopic_dropdown_list_options.html', {'subtopics': subtopics})

class SearchResultsView(ListView):
    model = Topic
    template_name = 'search_results.html'