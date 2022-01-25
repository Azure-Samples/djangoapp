from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from papermasters.models import topic


def index(request):
    return HttpResponse("Hello, world. You're at the Paper Masters index.")

class topicDetailView(DetailView):

    model = topic
    
class topic(DetailView):
    model = topicPkAndSlug
    query_pk_and_slug = False

