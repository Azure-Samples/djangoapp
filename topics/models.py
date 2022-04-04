from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 50)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    content_two = models.TextField(blank=True)
    lower_content = models.TextField(blank=True)
    old_url = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
            verbose_name = 'subject'
            verbose_name_plural = 'subjects'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
            return reverse('slug', args=[str(self.slug)])

class Subtopic(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length = 50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    content_two = models.TextField(blank=True)
    lower_content = models.TextField(blank=True)
    old_url = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
            verbose_name = 'subtopic'
            verbose_name_plural = 'subtopics'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
            return reverse('slug', args=[str(self.slug)])

class Topic(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length = 50)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    related = models.TextField(blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    old_url = models.CharField(max_length=255, blank=True)
    new_url = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'topic'
        verbose_name_plural = 'topics'
            
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
            return reverse('slug', args=[str(self.slug)])
