
from django import forms


class FormInstruct(forms.Form):
    label = forms.CharField(max_length=100)
    shell = forms.CharField(max_length=100)
    os = forms.CharField(max_length=60)
    admin = forms.BooleanField()


__all__ = [
    "FormInstruct"
]