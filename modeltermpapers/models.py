from django.db import models

class mtpPage(models.Model):
    meta_title = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=250)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)

#    def __str__(self):
#        return self.name