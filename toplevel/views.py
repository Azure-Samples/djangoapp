from django.shortcuts import render
from django.http import HttpResponse


def toplevelView(request):
    return render(request, 'toplevel/toplevel.html')
