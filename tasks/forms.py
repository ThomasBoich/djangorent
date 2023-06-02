from django import forms

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

    class Meta:
        model = Task
        fields = ['title','text','date_start','date_finish','owner','executor','object']