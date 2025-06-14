# admissions/forms.py
from django import forms
from .models import Application, Document

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'email', 'phone', 'applied_course']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['doc_name', 'file']
