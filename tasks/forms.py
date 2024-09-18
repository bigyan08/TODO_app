from django import forms
from django.forms import ModelForm

from .models import *

#model forms 
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task # we are going to create a model form for Task model
        fields= '__all__'