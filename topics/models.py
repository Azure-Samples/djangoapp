from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.utils.text import slugify
from django.urls import reverse
from datetime import datetime
from mptt.fields import TreeManyToManyField


class Category(MPTTModel):
    parent = TreeForeignKey("self", on_delete=models.CASCADE, 
    blank=True, null=True, related_name="children"
    )
    title = models.CharField(_("Title"), max_length=200)

    class Meta:
        ordering = ["tree_id", "lft"]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    class MPTTMeta:
        order_insertion_by = ["title"]

    def __str__(self):
        return self.title


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
    categories = TreeManyToManyField(
        "categories.Category",
        verbose_name=_("Categories"),
        related_name="category_ideas",
    )

    def __str__(self):
        return self.topic_text

    def get_absolute_url(self):
        return reverse('slug', args=[str(self.slug)])
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)