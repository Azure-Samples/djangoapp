from django.contrib import admin
from .models import topic, subject, subtopic


admin.site.register(subject)



class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('subtopic_text', 'subject', 'slug')
    ordering = ('subject', 'subtopic_text')
    search_fields = ('topic_text', 'content')

admin.site.register(subtopic, SubtopicAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic_text', 'subject', 'subtopic', 'new_url', 'update_date')
    ordering = ('id', 'subject', 'subtopic', 'topic_text')
    search_fields = ('topic_text', 'content')

admin.site.register(topic, TopicAdmin)