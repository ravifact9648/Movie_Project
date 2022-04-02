from django import forms
from testapp.models import Movie
from django.contrib.auth.models import User
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'



class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name']

