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
    old_url = models.CharField(max_length=200,blank=True)
    lower_content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
            verbose_name = 'service'
            verbose_name_plural = 'services'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('slug', args=[str(self.slug)])
