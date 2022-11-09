from django.forms import ModelForm

from .models import tasklist


class todo_task(ModelForm):
    class Meta:
        model = tasklist
        fields = ['title','memo','important']