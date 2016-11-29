from django.shortcuts import render
# Create your views here.
from models import Url
from django.http import HttpResponse,  HttpResponseRedirect
from Url_cls import Url_c

def index(request):
    if request.method == 'POST':
        Surl = Url_c.L2S_url(request.POST.get('longurl'))
        return render(request, 'index.html', {'Surl':Surl, 'Lurl':request.POST.get('longurl')})
    return render(request, 'index.html')


def get_url(request, Surl=None):
    Lurl = Url_c.S2L_url(Surl)
    return HttpResponseRedirect(Lurl)
