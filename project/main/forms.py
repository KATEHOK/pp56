from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

class AddPetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['species'].empty_label = 'Вид не выбран'
        self.fields['owner'].empty_label = 'Хозяин не выбран'

    class Meta:
        model = Pet
        fields = ['name', 'slug', 'description', 'photo', 'species', 'owner', 'is_published']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input_txt'}),
            'slug': forms.TextInput(attrs={'class': 'input_txt'}),
            'description': forms.Textarea(attrs={'class': 'input_txt_area'}),
        }
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 30:
            raise ValidationError('Длина превышает 30 символоов')
        return name

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if len(slug) > 60:
            raise ValidationError('Длина превышает 60 символоов')
        return slug


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input_txt'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'input_txt'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input_txt'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'input_txt'}))
    class Meta:
        model = Person
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input_txt'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input_txt'}))
