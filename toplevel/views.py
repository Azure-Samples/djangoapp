from importlib import resources
from django.shortcuts import render
from django.http import HttpResponse
from toplevel.models import Service


def toplevel_view(request):
    return render(request, 'toplevel/toplevel.html')

def toplevel_view(request): 
    toplevel_objects = Service.objects.all()
    return render(request, 'toplevel/toplevel.html', {'toplevel_objects':toplevel_objects})
