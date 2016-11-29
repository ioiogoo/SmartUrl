from django.shortcuts import render
# Create your views here.
from models import Url
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        return HttpResponse(request.POST.get('longurl'))
    return render(request, 'index.html')
