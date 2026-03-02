"""Forms for the notices application."""

from django import forms
from .models import Notice


class NoticeForm(forms.ModelForm):
    """Form for creating and editing notices."""
    
    class Meta:
        model = Notice
        fields = ['title', 'content', 'author', 'is_pinned']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter notice title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter notice content',
                'rows': 6
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name or organization'
            }),
            'is_pinned': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
