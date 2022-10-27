from django.contrib import admin
from .models import Topic, Subject, Subtopic


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    ordering = ('id', 'name')
    search_fields = ('name', 'content')

admin.site.register(Subject, SubjectAdmin)


class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'subject', 'slug')
    ordering = ('id','subject', 'name')
    search_fields = ('name', 'content')

admin.site.register(Subtopic, SubtopicAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'subtopic', 'new_url')
    ordering = ('id', 'subject', 'subtopic', 'name')
    search_fields = ('name', 'content')

admin.site.register(Topic, TopicAdmin)
