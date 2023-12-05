from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserAccount, UserProfile


class userRegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Enter your email'}))

    password1 = forms.CharField(required=True, label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Enter a password'}))
    password2 = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'confirm_password', 'placeholder': 'Confirm password'}))
    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Enter a username'}))

    full_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter your name'}))

    class Meta:
        model = UserAccount
        fields = ['username', 'full_name', 'email']


class userLoginForm(AuthenticationForm):

    error_messages = {
        'invalid_login': 'Please enter a correct username and password.',
        'inactive': 'This account is inactive.'
    }

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control custom-input'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control custom-input'}))


class userProfileForm(forms.ModelForm):
    about = forms.CharField(label='About Me', required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '3', 'style': 'resize:none'}))
    area = forms.CharField(label='Area', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    domain = forms.CharField(label='Domain', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    whatsApp_no = forms.CharField(label='WhatsApp No', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    phone_no = forms.CharField(label='Phone No', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    phone_same_as_whatsapp = forms.BooleanField(
        label='Same as above', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    country = forms.CharField(label='Country', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    state = forms.CharField(label='State', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    city = forms.CharField(label='City', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('about', 'area', 'domain', 'whatsApp_no', 'phone_no',
                  'phone_same_as_whatsapp', 'country', 'state', 'city', 'address')
