from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core import validators
from .models import CustomUser


# ----------------------------------------------------------
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


# ----------------------------------------------------------
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


# ----------------------------------------------------------
class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email', 'class': 'woocommerce-Input woocommerce-Input--text input-text'}),
        label='Email',
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password', 'class': 'woocommerce-Input woocommerce-Input--text input-text'}),
        label='Password',
        required=True,
    )

    remember_me = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'class': 'woocommerce-form__input woocommerce-form__input-checkbox'}),
        required=False,
        initial=False,
        label='Remember me',
    )


# ----------------------------------------------------------
class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email', 'class': 'woocommerce-Input woocommerce-Input--text input-text'}),
        required=True,
        label='Email',
        validators=[validators.EmailValidator(message='Please enter a valid email')]
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'id': 'phone', 'type': 'tel', 'class': 'woocommerce-Input woocommerce-Input--text input-text',
                   'placeholder': 'Phone Number',
                   }),
        required=True,
        label='Phone Number'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'id': 'password', 'placeholder': 'Password',
                   'class': 'woocommerce-Input woocommerce-Input--text input-text'}),
        required=True,
        label='Password',
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'id': 'password_confirm', 'placeholder': 'Confirm password',
                   'class': 'woocommerce-Input woocommerce-Input--text input-text'}),
        required=True,
        label='Confirm Password',
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists = CustomUser.objects.filter(email=email).exists()
        if is_exists:
            raise forms.ValidationError('Email is already taken')
        return email

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise forms.ValidationError('Password and confirm password does not match')
        return confirm_password

    class ForgetPass(forms.Form):
        pass
