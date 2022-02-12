from django.shortcuts import render
from resources.models import Resource

def resource_view(request, slug):
    slug = slug
    rg = Resource.objects.get(slug=slug)
    context = {
        'title':rg.title,
        'content':rg.content,
        'meta_description':rg.meta_description,
        'meta_title':rg.meta_title,
    }
    return render(request, 'resources/resource.html', context)
