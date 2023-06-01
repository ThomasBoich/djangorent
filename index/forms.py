from django import forms

from index.models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'})
    )
    phone = forms.CharField(label='',
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Введите ваш телефон'})
    )
    email = forms.EmailField(label='',
        widget=forms.EmailInput(attrs={'placeholder': 'Введите ваш email'})
    )
    message = forms.CharField(label='',
        widget=forms.Textarea(attrs={'placeholder': 'Введите ваше сообщение', 'cols': 23,})
    )

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'message']