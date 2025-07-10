from django import forms


class TestForm(forms.Form):
    num = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)