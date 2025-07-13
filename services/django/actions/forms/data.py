
from django import forms

class FormSoft(forms.Form):
    name = forms.CharField(max_length=100)
    execute = forms.CharField(max_length=100)
    path = forms.CharField(max_length=100)


__all__ = [
    "FormSoft"
]