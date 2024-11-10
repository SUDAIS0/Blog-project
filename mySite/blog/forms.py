from django import forms

from .models import Comments

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
