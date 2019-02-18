from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create your forms here.
class Registrationform(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'password2',
        ]

class editUser(UserChangeForm):
    class Meta:
        model=User
        fields=[
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
        ]