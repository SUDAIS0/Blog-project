from django import forms

from .models import Comments, User
from django.core.exceptions import ValidationError
import re
import dns.resolver         # For email domain validation
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class PostCommentsForm(forms.ModelForm):
    
    class Meta:
        model = Comments

        fields = ['comment']

        labels = {
            'comment' : "Comments"
        }

        error_messages = {
            'comment' :{
                'required' : "You must have to type a comment."
            }
        }

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput, min_length=8, required=True, help_text="Password must be at least 8 characters long, include at least one uppercase letter, one symbol, and one digit.")
    password_confirm = forms.CharField(widget=forms.PasswordInput, required=True, help_text="Confirm your password")
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        error_messages = {
            'username' : {
                'required' : "You Havent Enterd your name yet",
                'max_length' : "Max Length is 70 Chrahcters only"
            },
            'email' :{
                'required' : "You must have to type a comment."
            }
        }

        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        # Check if passwords match
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")

        # Check for at least one uppercase letter
        if password and not any(char.isupper() for char in password):
            self.add_error('password', "Password must include at least one uppercase letter.")

        # Check for at least one digit
        if password and not any(char.isdigit() for char in password):
            self.add_error('password', "Password must include at least one digit.")

        # Check for at least one special symbol
        if password and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            self.add_error('password', "Password must include at least one symbol.")

        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            domain = email.split('@')[1]
            dns.resolver.resolve(domain, 'MX')
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            raise ValidationError("The email domain does not exist or is not capable of receiving emails.")
        return email

class AccountSettingForm(forms.Form):

    first_name = forms.CharField(max_length=30, required=True, error_messages={
        'required': "You must enter your first name."
    })
    last_name = forms.CharField(max_length=30, required=True, error_messages={
        'required': "You must enter your last name."
    })
    email = forms.EmailField(required=True, error_messages={
        'required': "You must enter an email address."
    })
    username = forms.CharField(max_length=150, required=True, error_messages={
        'required': "You must enter a username.",
        'max_length': "Username cannot exceed 150 characters."
    })

    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    password_confirm = forms.CharField(widget=forms.PasswordInput)


    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            domain = email.split('@')[1]
            dns.resolver.resolve(domain, 'MX')
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            raise ValidationError("The email domain does not exist or is not capable of receiving emails.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        # Check if passwords match
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")

        # Check for at least one uppercase letter
        if password and not any(char.isupper() for char in password):
            self.add_error('password', "Password must include at least one uppercase letter.")

        # Check for at least one digit
        if password and not any(char.isdigit() for char in password):
            self.add_error('password', "Password must include at least one digit.")

        # Check for at least one special symbol
        if password and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            self.add_error('password', "Password must include at least one symbol.")

        return cleaned_data
    
        
