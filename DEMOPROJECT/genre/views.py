from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def gen(request):
    return HttpResponse("<h1> Hey Genre coming</h1>")