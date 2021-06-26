from django.contrib.auth.models import User
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from .models import logindb, userdb
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class loginform(forms.ModelForm):
    username = forms.CharField(label ='',max_length=100, widget= forms.TextInput(attrs={'placeholder':'ENTER USERNAME'}))
    password = forms.CharField(label= '',max_length=100, widget= forms.PasswordInput(attrs={'placeholder':'ENTER PASSWORD'}))
    class Meta:
        model = logindb
        fields ="__all__"



class registerform(forms.ModelForm):
    class Meta:
        model = userdb
        fields ="__all__"

    def clean_username(self):  # Validates the  Field
        u_name = self.cleaned_data.get('username')
        if (u_name == ""):
            raise forms.ValidationError('This field cannot be left blank')
        return u_name

    # def clean_email(self):  # Validates the email
    #     email = self.cleaned_data.get('email')
    #     if (email == ""):
    #         raise forms.ValidationError('This field cannot be left blank')
    #     for instance in userdb.objects.all():
    #         if instance.email == email:
    #             raise forms.ValidationError(email + ' is already added')
    #     return email



    def word_exists(value,email):
        if userdb.objects.filter(email=email).exists():
            raise ValidationError("The word already exists!")


