from django.contrib import admin
from .models import topic, subject


admin.site.register(subject)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_text', 'subject', 'subtopic', 'update_date')
    ordering = ('topic_text',)
    search_fields = ('topic_text', 'content')

admin.site.register(topic, TopicAdmin)
