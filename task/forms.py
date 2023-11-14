from django import forms
from .models import Task

# Usando modelForm
"""
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
"""
# Usando Form
class TaskForm(forms.Form):
    tittle = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    completed = forms.BooleanField(required=False)