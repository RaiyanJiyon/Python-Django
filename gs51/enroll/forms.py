from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {'name': 'Full Name:', 'email': 'Enter Email:', 'password': 'Enter Password:'}
        widgets = {
            'password': forms.PasswordInput,
        }