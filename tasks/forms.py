from django import forms
from django.forms import widgets

from .models import TaskComment, Task


class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = TaskComment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Введите комментарий'})
        }

class addTaskForm(forms.ModelForm):
    #photo = MultiImageField(max_file_size=1024 * 1024 * 5, required=False)
    date_start = forms.DateTimeField(widget=widgets.DateTimeInput(attrs={'type': 'datetime-local'}))
    date_finish = forms.DateTimeField(widget=widgets.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Task
        fields = ['title','text','date_start','date_finish','owner','executor','object']