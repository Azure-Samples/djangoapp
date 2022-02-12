from django.contrib import admin
from .models import topic, subject, subtopic


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id','subject_text', 'slug')
    ordering = ('id', 'subject_text')
    search_fields = ('subject_text', 'content')

admin.site.register(subject, SubjectAdmin)



class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('id','subtopic_text', 'subject', 'slug')
    ordering = ('id','subject', 'subtopic_text')
    search_fields = ('topic_text', 'content')

admin.site.register(subtopic, SubtopicAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic_text', 'subject', 'subtopic', 'new_url', 'update_date')
    ordering = ('id', 'subject', 'subtopic', 'topic_text')
    search_fields = ('topic_text', 'content')

admin.site.register(topic, TopicAdmin)