from django.db import models
from treebeard.mp_tree import MP_Node
from django.utils.text import slugify
from django.urls import reverse
from datetime import datetime


class Category(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __str__(self):
        return 'Category: {}'.format(self.name)


class topic(models.Model):
    id = models.IntegerField(primary_key=True)
    topic_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length = 255, null = True, blank = True)
    meta_title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    related = models.TextField(blank=True)
    old_url = models.CharField(max_length=255, blank=True)
    new_url = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic_text

    def get_absolute_url(self):
        return reverse('slug', args=[str(self.slug)])
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)