from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Электронная почта')
    first_name = forms.CharField(required=True, label='Имя')
    last_name = forms.CharField(required=True, label='Фамилия')
    patronymic = forms.CharField(required=False, label='Отчество')
    phone = forms.CharField(required=False, label='Телефон')

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'patronymic', 'phone', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True, label='Электронная почта')
    first_name = forms.CharField(required=True, label='Имя')
    last_name = forms.CharField(required=True, label='Фамилия')
    patronymic = forms.CharField(required=False, label='Отчество')
    phone = forms.CharField(required=False, label='Телефон')

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'patronymic', 'phone', 'photo', 'type')

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['photo'].required = False


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']


class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'patronymic', 'phone', 'photo']
        exclude = ['username', 'sender']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'