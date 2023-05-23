from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.utils.text import slugify
from .models import Object, Reservation
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

class ReservationEditForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guest_last_name', 'guest_first_name', 'guest_patronymic', 'guest_email', 'guest_phone']

    guest_last_name = forms.CharField(max_length=255, label='Фамилия')
    guest_first_name = forms.CharField(max_length=255, label='Имя')
    guest_patronymic = forms.CharField(max_length=255, label='Отчество')
    guest_email = forms.EmailField(label='Емейл')
    guest_phone = forms.CharField(max_length=20, label='Телефон')