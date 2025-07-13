from django.http import HttpRequest, HttpResponse

from lib.sys import system
from lib import resolver
from pathlib import Path
from .forms import data, instruct

controlor = system.System()
def send_instruct(requets: HttpRequest):
    if requets.method == "GET":
        form = instruct.FormInstruct(requets.GET)

        label = form.cleaned_data['label']
        shell = form.cleaned_data['shell']

        report = controlor.executor(shell)
        return HttpResponse(report)
    else:
        return HttpResponse("null")
    


def start_software(request: HttpRequest):
    if request.method == "POST":
        form = data.FormSoft(request)

        execute = form.cleaned_data['execute']
        path = form.cleaned_data['path']
        path = Path(path).joinpath(execute)
        report = controlor.start_software(path)
        return HttpResponse(report)
    else:
        return HttpRequest("null")
    

__all__ = [
    "send_instruct",
    "start_software",
]