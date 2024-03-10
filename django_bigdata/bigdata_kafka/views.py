from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    data={
        'data':'data'
    }
    return render(request,'index.html',data)