from pathlib import Path

from django import forms
from multiupload.fields import MultiImageField
from django.contrib.auth.forms import UserChangeForm
from django.utils.text import slugify
from .models import Object, Reservation, ObjectPhoto
from unidecode import unidecode


class ObjectPhotoForm(forms.ModelForm):
    photo = MultiImageField(max_file_size=1024*1024*5, required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.photo:
            filename = Path(self.instance.photo.name).name
            self.fields['photo'].label = filename

    class Meta:
        model = ObjectPhoto
        fields = ['photo']
        labels = {'photo': 'Object Photo', 'name': 'Object Photo',}

class addObjectForm(forms.ModelForm):
    #photo = MultiImageField(max_file_size=1024 * 1024 * 5, required=False)

    class Meta:
        model = Object
        fields = [
        'name_ru', 'name_en', 'top_photo',
        'features_ru',
        'features_en','text_ru',
        'text_en','description_ru',
        'description_en','address','coordinates_x','coordinates_y','bad_coordinates_x','bad_coordinates_y',
        'city_ru','city_en','country_ru','country_en',
        'price_ru','price_en','rating'
        ]
        labels = {'name': 'name_en', 'description': 'Description', 'location': 'Location', 'price': 'Price','features_ru': 'Опции на Русском', 'slug': 'Оставить пустым!'}
        widgets = {
            'name_ru': forms.TextInput(attrs={'placeholder': 'Введите название на русском'}),
            'name_en': forms.TextInput(attrs={'placeholder': 'Enter the name in English'}),
            'description_ru': forms.Textarea(attrs={'placeholder': 'Введите описание на русском'}),
            'description_en': forms.Textarea(attrs={'placeholder': 'Enter the description in English'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter the address'}),
            'coordinates_x': forms.TextInput(attrs={'placeholder': 'Enter X coordinates'}),
            'coordinates_y': forms.TextInput(attrs={'placeholder': 'Enter Y coordinates'}),
            'bad_coordinates_x': forms.TextInput(attrs={'placeholder': 'Enter bad X coordinates'}),
            'bad_coordinates_y': forms.TextInput(attrs={'placeholder': 'Enter bad Y coordinates'}),
            'price_ru': forms.NumberInput(attrs={'placeholder': 'Enter the price in rubles'}),
            'price_en': forms.NumberInput(attrs={'placeholder': 'Enter the price in dollars'}),
        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'] = forms.CharField(required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        slug = slugify(unidecode(str(instance.name_en)))
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