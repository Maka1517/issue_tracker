from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from .models import STATUS_CHOICES,TYPE_CHOICES, Issue

default_status = STATUS_CHOICES[0][0]
default_type = TYPE_CHOICES[0][0]

BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'



class IssuesForm(forms.ModelForm):
    summary = forms.CharField(max_length=200, required=True, label='Заголовок')
    description = forms.CharField(max_length=3000, required=False, label='Описание', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='Статус')
    issue_type = forms.ChoiceField(choices=TYPE_CHOICES, initial=default_type, label='Тип')
    created_at = forms.DateTimeField(required=False, label='Время записи',
                                     input_formats=['%Y-%m-%d', BROWSER_DATETIME_FORMAT,
                                                    '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
                                                    '%Y-%m-%d %H:%M:%S'],
                                     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError('Title is too short!')
        return title

    def clean(self):
        cleaned_data = super().clean()
        errors = []
        description = cleaned_data.get('description')
        summary = cleaned_data.get('summary')
        if description and summary and description == summary:
            errors.append(ValidationError("Text of the description should not duplicate it's summary!"))
        if errors:
            raise ValidationError(errors)
        return cleaned_data