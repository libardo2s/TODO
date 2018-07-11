from django.forms import ModelForm, TextInput, DateInput, forms, HiddenInput

from .models import Todo


class FormAdd(ModelForm):
    class Meta:
        model = Todo
        fields = ('task', 'description',)
        widgets = {
            'task': TextInput(attrs={'class': "form-control"}),
            'description': TextInput(attrs={'class': "form-control"}),
        }


class FormUpdate(ModelForm):
    class Meta:
        model = Todo
        fields = ('id', 'task', 'description',)
        widgets = {
            'id': TextInput(attrs={'class': "form-control", 'id': 'id_update'}),
            'task': TextInput(attrs={'class': "form-control", 'id': 'task_update'}),
            'description': TextInput(attrs={'class': "form-control", 'id': 'description_update'}),
        }