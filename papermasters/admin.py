from django.contrib import admin
from .models import topic, subject, subtopic


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_text')

admin.site.register(subject, SubjectAdmin)

class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('subtopic_text')

admin.site.register(subtopic, SubtopicAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_text', 'subject', 'subtopic', 'update_date')
    ordering = ('topic_text',)
    search_fields = ('topic_text', 'content')

admin.site.register(topic, TopicAdmin)