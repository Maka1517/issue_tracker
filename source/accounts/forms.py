from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
        field_classes = {'username': UsernameField}

    def clean(self):
        cleaned_data = super(MyUserCreationForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not first_name and last_name:
            raise forms.ValidationError('Вы не заполнили поле first_name или last_name')

