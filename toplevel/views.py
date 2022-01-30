from importlib import resources
from django.shortcuts import render
from django.http import HttpResponse


def toplevel_view(request):
    return render(request, 'toplevel/toplevel.html')

