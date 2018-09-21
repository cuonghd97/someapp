from django import forms

class userInfo(forms.Form):
    userName = forms.CharField(label='username', max_length=None)
    email = forms.CharField(label='email', max_length=None)
    birthday = forms.CharField(label='birthday', max_length=None)