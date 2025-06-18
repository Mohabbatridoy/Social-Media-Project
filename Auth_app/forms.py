from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'username','class':'form-control'}))
    password1 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder':'Password',})
    )
    password2 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation',})
    )
    class Meta:
        model = User
        fields = ('username','email','password1','password2')