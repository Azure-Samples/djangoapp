from django.db import models
from django.utils.text import slugify
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
        return reverse('slug', args=[str(self.slug)])
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)