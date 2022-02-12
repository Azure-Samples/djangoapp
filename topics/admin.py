from django.contrib import admin
from .models import topic, subject, subtopic


admin.site.register(subject)



class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('subtopic_text', 'subject', 'slug',)
    ordering = ('subject', 'subtopic_text')
    search_fields = ('topic_text', 'content')

admin.site.register(subtopic, SubtopicAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_text', 'subject', 'subtopic', 'update_date',)
    ordering = ('subject', 'subtopic', 'topic_text')
    search_fields = ('topic_text', 'content')

admin.site.register(topic, TopicAdmin)