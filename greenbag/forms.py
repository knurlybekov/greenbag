# # accounts/forms.py
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#
# from .models import CustomUser
#
#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ("username", "email")
#
#
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ("username", "email")
# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']  # Add other fields you want to include in your form


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password', 'username', 'image', 'date_of_birth']  # Add other fields you wish to be editable