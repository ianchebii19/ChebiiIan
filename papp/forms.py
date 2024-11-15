from django import forms
from .models import ContactMessage
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class LoginForm(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'autocomplete':'current-password','class': 'form-control'}))

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']