from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def aru(request):
    return HttpResponse('<h2>hello</h2>')