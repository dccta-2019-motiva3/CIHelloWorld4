from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>hello world</h1>")