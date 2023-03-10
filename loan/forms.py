from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Loans


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

class LoansForm():
    class Meta:
        model = Loans
        fields = "__all__"