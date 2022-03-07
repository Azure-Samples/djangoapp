from django.contrib import admin
from .models import topic, Category

admin.site.register(Category)


admin.site.register(topic)
