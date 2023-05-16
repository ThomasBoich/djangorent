from django import forms
from django.utils.text import slugify
from .models import Object
from unidecode import unidecode


class addObjectForm(forms.ModelForm):

    class Meta:
        model = Object
        fields = ['name', 'photo', 'features', 'text', 'description', 'address', 'city', 'country', 'price', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'] = forms.CharField(required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        slug = slugify(unidecode(instance.name))
        instance.slug = slug
        if commit:
            instance.save()
        return instance