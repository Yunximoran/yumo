from django import forms


class Question(forms.Form):
    question = forms.CharField()

