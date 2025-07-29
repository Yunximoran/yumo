from django.http import HttpRequest, HttpResponse, Http404
from django.contrib import admin
from .. import actions
from ..signal import first

def view(request: HttpRequest):
    if request.method == "GET":
        usrid =  request.GET.get("usrid")
        if usrid:
            s = actions.user.login(usrid)
        return HttpResponse("<h1>云曦墨染的杂货铺</h1>")
    return HttpResponse("error")



def answer_aigc(request: HttpRequest):
    if request.method == "POST":
        question = request.POST.get("question")
        answer = actions.aigc.answer(question)
        return HttpResponse(answer)
    return Http404("method is error please use post")
        

    