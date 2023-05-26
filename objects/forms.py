from django import forms
from multiupload.fields import MultiImageField
from django.contrib.auth.forms import UserChangeForm
from django.utils.text import slugify
from .models import Object, Reservation, ObjectPhoto
from unidecode import unidecode


# class ObjectPhotoForm(forms.ModelForm):
#     photo = MultiImageField(max_file_size=1024*1024*5, required=False)
#
#     class Meta:
#         model = ObjectPhoto
#         fields = ('photo',)


class addObjectForm(forms.ModelForm):

    class Meta:
        model = Object
        fields = [
        'name_ru', 'name_en',
        'photo','features_ru',
        'features_en','text_ru',
        'text_en','description_ru',
        'description_en','address','coordinates','bad_ccordinates',
        'city_ru','city_en','country_ru','country_en',
        'price_ru','price_en','rating'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'] = forms.CharField(required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        slug = slugify(unidecode(instance.name_en))
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