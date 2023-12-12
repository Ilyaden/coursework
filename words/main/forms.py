from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re
from django.core.exceptions import ValidationError
from .models import *

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        )
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))


class StartGameForm(forms.ModelForm):

    class Meta:
        model = Game 
        fields = ['username', 'username2', 'word']
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'username2' : forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'word' :forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        
        }

    def clean_word(self):
        word = self.cleaned_data['word']
        if not re.match("^[а-яё]+$", word):
            raise forms.ValidationError("Слово должно состоять только из русских букв в нижнем регистре.")

        return word

class GameForm(forms.Form):

    letter = forms.CharField(max_length=1, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    def clean_letter(self):
        letter = self.cleaned_data['letter']
        if not re.match("^[а-яё]+$", letter):
            raise forms.ValidationError("Буква должна состоять только из русских символов в нижнем регистре.")

        return letter


   

    
    
        
        