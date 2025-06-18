from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Task Title',
            'description': 'Task Description',
            'completed': 'Completed',
        }
        help_texts = {
            'title': 'Enter the title of the task.',
            'description': 'Enter a detailed description of the task.',
            'completed': 'Check if the task is completed.',
        }

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Task Title',
            'description': 'Task Description',
            'completed': 'Completed',
        }
        help_texts = {
            'title': 'Enter the title of the task.',
            'description': 'Enter a detailed description of the task.',
            'completed': 'Check if the task is completed.',
        }

class TaskDeleteForm(forms.ModelForm):  
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {}
        help_texts = {}
        error_messages = {}
