from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']


# here we created a new field with our default form given by DJANGO for the user
# registration and needs to be filled as well
# at the last all data is kept inside fields
