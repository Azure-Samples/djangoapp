from django.contrib import admin
from .models import topic

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic_text', 'new_url')
    ordering = ('id', 'topic_text')
    search_fields = ('topic_text', 'content')

admin.site.register(topic, TopicAdmin)
