from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Resource(models.Model):
    id =  models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null = True, unique = True, blank = True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=400)
    content = models.TextField(blank=True)
    old_url = models.CharField(max_length=200,blank=True)
    lower_content = models.TextField(blank=True)
    TYPE_OF_RESOURCE = (
        ('E', 'Elements of a Paper'),
        ('R', 'Type of Research'),
        ('P', 'Type of Paper'),
    )
    type_of_resource = models.CharField(max_length=1, choices=TYPE_OF_RESOURCE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    class Meta:
            verbose_name = 'resource'
            verbose_name_plural = 'resources'
    
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('resource_detail', kwargs={'slug': self.slug})
