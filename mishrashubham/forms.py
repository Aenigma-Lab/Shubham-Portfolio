# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'comments']  # Specify the fields to include in the form

        # Optionally, you can add custom widgets or labels here
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Your Message'}),
        }
        labels = {
            'name': 'Your Name',
            'email': 'Email Address',
            'comments': 'Your Message',
        }
