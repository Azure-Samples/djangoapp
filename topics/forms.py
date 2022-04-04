from django import forms
from .models import Topic, Subtopic

class TopicForm(forms.Form):
    class Meta:
        model = Topic
        fields = ('id','name', 'subject', 'subtopic', 'slug', 'meta_title', 'meta_description', 'related','old_url', 'new_url','created','updated')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subtopic'].queryset = Subtopic.objects.none()

        if 'subject' in self.data:
            try:
                subject_id = int(self.data.get('subject'))
                self.fields['subtopic'].queryset = Subtopic.objects.filter(subject_id=subject_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['subtopic'].queryset = self.instance.subject.subtopic_set.order_by('name')