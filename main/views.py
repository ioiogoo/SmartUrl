from django.shortcuts import render
# Create your views here.
# from models import Url
from django.http import HttpResponse,  HttpResponseRedirect
from Url_cls import Url_c
import re
from .models import Url

def index(request):
    if request.method == 'POST':
        Surl, Views = Url_c.L2S_url(request.POST.get('longurl'))
        return render(request, 'index.html', {'Surl':Surl, 'Lurl':request.POST.get('longurl'), 'Views': Views})
    return render(request, 'index.html')


def get_url(request, Surl=None):
    try:
        Lurl = Url_c.S2L_url(Surl)
        url = Url.objects.filter(Lurl=Lurl)[0]
        url.Views += 1
        url.save()
    except Exception as e:
        return HttpResponseRedirect('/')
    return HttpResponseRedirect(Lurl)


