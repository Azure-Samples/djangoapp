from django.shortcuts import render
from toplevel.models import Service

def IndexView(request):
        return render(request, 'toplevel/index.html')

def services_view(request, slug):
    slug = slug
    sg = Service.objects.get(slug=slug)
    context = {
        'title':sg.title,
        'content':sg.content,
        'meta_description':sg.meta_description,
        'meta_title':sg.meta_title,
    }
    return render(request, 'toplevel/services.html', context)

def toplevel_view(request): 
    toplevel_objects = Service.objects.all()[:3]
    return render(request, 'toplevel/toplevel.html', {'toplevel_objects':toplevel_objects})
