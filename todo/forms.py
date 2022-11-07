from django import forms
from .models import *


class Taskform(forms.ModelForm):
    class Meta:
        model = tasklist
        fields = ['task','done']