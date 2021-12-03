from .models import Task
from django import forms
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'


class UpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'priority', 'created_at')
        widgets = {
            'created_at': DateInput()
        }
