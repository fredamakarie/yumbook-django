# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Form for registering new users."""
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "bio",
            "profile_picture",
            "password1",
            "password2",
        )


class CustomUserChangeForm(UserChangeForm):
    """Form for updating user profile (used in admin and profile edit)."""
    password = None  # Hide password field if you don't want it in profile edit

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "bio",
            "profile_picture",
        )
