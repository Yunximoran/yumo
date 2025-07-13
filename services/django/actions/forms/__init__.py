from django import forms

from .data import *
from .instruct import *

class TestForm(forms.Form):
    num = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)