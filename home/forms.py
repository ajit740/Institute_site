from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'phone', 'course', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us anything you want...'}),
        }
