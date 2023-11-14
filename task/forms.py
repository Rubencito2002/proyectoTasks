from django import forms
#from .models import Task

# Usando modelForm
"""
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
"""
# Usando Form
class TaskForm(forms.Form):
    tittle = forms.CharField(label="tittle", max_length=200)
    description = forms.CharField(label="description", widget=forms.Textarea)
    completed = forms.BooleanField(label="completed", required=False)