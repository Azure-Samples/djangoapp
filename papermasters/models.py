from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class subject(models.Model):
    name = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    content_two = models.TextField(blank=True)
    lower_content = models.TextField(blank=True)
    old_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class subtopic(models.Model):
    subtopic_text = models.CharField(max_length=200)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.subtopic_text

class topic(models.Model):
    topic_text = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    meta_title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    related = models.TextField(blank=True)
    image = models.ImageField(upload_to='static/images', blank=True)
    image_url = models.URLField(blank=True)
    lower_content = models.TextField(blank=True)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(subtopic, on_delete=models.CASCADE)
    old_url = models.URLField(blank=True)
    update_date = models.DateTimeField('Last Updated', default='2022-01-31T15:58:44.767594-06:00')

    def __str__(self):
        return self.topic_text

    def get_absolute_url(self):
        return reverse('slug', args=[str(self.slug)])
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)
   

