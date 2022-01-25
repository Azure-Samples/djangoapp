from django.db import models
from django.urls import reverse
import itertools

class subject(models.Model):
    name = models.CharField(max_length=100)

class subtopic(models.Model):
    subtopic_text = models.CharField(max_length=200)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)

class topic(models.Model):
    topic_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True)
    description = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    related = models.TextField(blank=True)
    image = models.ImageField(upload_to='papermasters/media/images', blank=True)
    image_url = models.URLField(blank=True)
    lower_content = models.TextField(blank=True)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(subtopic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={'slug': self.slug})
        
class topicUniqueSlug(topic):

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = self.topic_text
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not topicUniqueSlug.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)