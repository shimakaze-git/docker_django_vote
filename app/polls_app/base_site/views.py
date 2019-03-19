from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        context = {}
        # return HttpResponse('test')
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        context = {}
        # return HttpResponse('test')
        return render(request, self.template_name, context)


def index(request):
    context = {}
    # return HttpResponse('test')
    return render(request, 'index.html', context)
