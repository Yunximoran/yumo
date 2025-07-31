from django.http import HttpRequest
from django.http import HttpResponse, StreamingHttpResponse
from django.http import Http404
from django.contrib import admin
from .. import actions


def view(request: HttpRequest):
    if request.method == "GET":
        usrid =  request.GET.get("usrid")
        if usrid:
            s = actions.user.login(usrid)
        return HttpResponse("<h1>云曦墨染的杂货铺</h1>")
    return HttpResponse("error")

        

    