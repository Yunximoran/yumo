from django.http import HttpRequest
from django.http import HttpResponse, StreamingHttpResponse
from django.http import Http404


from .. import actions
from .. import forms




async def answer(request: HttpRequest):
    if request.method == "POST":

        form = forms.aigc.Question(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            question = data.get("question", "什么是deepseek")
            return StreamingHttpResponse(
                await actions.aigc.answer(question),
                content_type="text/plain"
            )
        raise Http404("error")
    else:
        raise Http404("method is error please use post")