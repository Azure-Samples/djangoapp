from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from datetime import datetime 

class subject(models.Model):
    id = models.IntegerField(primary_key=True)
    subject_text = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 255, blank = True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    content_two = models.TextField(blank=True)
    lower_content = models.TextField(blank=True)
    old_url = models.CharField(max_length=255, blank=True)
    

    def __str__(self):
        return self.subject_text
    
    def get_absolute_url(self):
        return reverse('slug', args=[str(self.slug)])
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)

class subtopic(models.Model):
    id = models.IntegerField(primary_key=True)
    subtopic_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length = 255, blank = True)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    content_two = models.TextField(blank=True)
    lower_content = models.TextField(blank=True)
    old_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.subtopic_text
    
    def get_absolute_url(self):
        return reverse('slug', args=[str(self.slug)])
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)

class topic(models.Model):
    id = models.IntegerField(primary_key=True)
    topic_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length = 255, null = True, blank = True)
    meta_title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    related = models.TextField(blank=True)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(subtopic, on_delete=models.CASCADE)
    old_url = models.CharField(max_length=255, blank=True)
    new_url = models.CharField(max_length=255, blank=True)
    update_date = models.DateTimeField('Last Updated', default=datetime.now())

    def __str__(self):
        return self.topic_text

    def get_absolute_url(self):
        return reverse('slug', args=[str(self.slug)])
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)