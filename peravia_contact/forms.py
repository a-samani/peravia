from django import forms
from django.core import validators


# ----------------------------------------------------------
class ContactForm(forms.Form):
    fullname = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'FullName'}),
        label='FullName')

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Email'}),
        label='Email',
        validators=[validators.EmailValidator(message='Please enter a valid email')])

    phone_number = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'id': 'phone',
                   'type': 'tel',
                   'class': 'form-control',
                   'placeholder': 'Phone Number'}),
        label='Phone Number')

    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Subject'}),
        label='Subject')

    enquiry = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'placeholder': 'Enquiry',
                   'rows': 8}),
        label='Enquiry'
    )

    def __init__(self, *args, **kwargs):
        lang = kwargs.pop('language', 'en')  # Default to 'en' if language is not provided
        super(ContactForm, self).__init__(*args, **kwargs)
        if lang == 'fa':
            self.fields['fullname'].widget.attrs['placeholder'] = 'نام کامل'
            self.fields['email'].widget.attrs['placeholder'] = 'ایمیل'
            self.fields['phone_number'].widget.attrs['placeholder'] = 'تلفن'
            self.fields['subject'].widget.attrs['placeholder'] = 'موضوع'
            self.fields['enquiry'].widget.attrs['placeholder'] = 'متن'
