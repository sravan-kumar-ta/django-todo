from .models import Task
from django.forms import ModelForm


class UpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'priority', 'created_at')
