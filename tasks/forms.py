from django import forms

from .models import TaskComment


class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = TaskComment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Введите комментарий'})
        }