from django import forms

from .models import Comments, User
from django.core.exceptions import ValidationError
import re

class PostCommentsForm(forms.ModelForm):
    
    class Meta:
        model = Comments

        fields = ['userName', 'comment']

        labels = {
            'userName' : "User Name",
            'comment' : "Comments"
        }

        error_messages = {
            'userName' : {
                'required' : "You Havent Enterd your name yet",
                'max_length' : "Max Length is 70 Chrahcters only"
            },
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
        print("runnign clean method")
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