from django import forms


class Login(forms.Form):
    email = forms.CharField(max_length=30)
    phone = forms.IntegerField()