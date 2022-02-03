from django.db import models
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from django.urls import reverse

class Service(models.Model):
    id =  models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null = True, unique = True, blank = True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=400)
    content = models.TextField(blank=True)
    old_url = models.URLField(blank=True)
    lower_content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('slug', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

        
class Resource(models.Model):
    id =  models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null = True, unique = True, blank = True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=400)
    content = models.TextField(blank=True)
    old_url = models.URLField(blank=True)
    lower_content = models.TextField(blank=True)
    TYPE_OF_RESOURCE = (
        ('E', 'Elements of a Paper'),
        ('R', 'Type of Research'),
        ('P', 'Type of Paper'),
    )
    type_of_resource = models.CharField(max_length=1, choices=TYPE_OF_RESOURCE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('resource_detail', kwargs={'slug': self.slug})
        
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
