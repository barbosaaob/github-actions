from django.views import View
from django.http import HttpResponse


class HelloWorld(View):
    def get(self, request):
        output = 'Hello world!<br>'
        if 'msg' in request.GET:
            output += 'Your message was: ' + request.GET['msg']

        return HttpResponse(output)
