from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import User, Donor
from captcha.fields import CaptchaField


class RegisterForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "captcha")


class DonerForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = "__all__"
        exclude = ("user", "last_donation_date")
        
