from django import forms


class UserLoginForm(forms.Form):
    """From to be used by user to login"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
