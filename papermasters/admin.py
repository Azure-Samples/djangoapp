from django.contrib import admin
from .models import topic, subject, subtopic

admin.site.register(subject)

admin.site.register(subtopic)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_text', 'subject', 'subtopic', 'update_date')
    ordering = ('topic_text',)
    search_fields = ('topic_text', 'content')

admin.site.register(topic, TopicAdmin)