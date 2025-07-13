from django.http import HttpRequest, HttpResponse


import json
def realtime(request):
    data = {

    }
    return HttpRequest(json.dumps(data))
