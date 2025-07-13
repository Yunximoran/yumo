from django import forms
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt

from services.django.actions.forms import TestForm
from .event import *

@csrf_exempt
@require_POST
def hello(request:HttpRequest):
    form = TestForm(request.POST)
    if form.is_valid():
        num = form.cleaned_data['num']
        name = form.cleaned_data['name']
        print(num ,type(num))
        print(name, type(name))
        return HttpResponse(f"{form.cleaned_data['num']}:-> {form.cleaned_data['name']}")
    return HttpRequest("None")
