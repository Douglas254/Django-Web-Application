from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
    return HttpResponse("<h1>WELCOME</h1>"
                        "<h2>This Python Django Website </h2>"
                        "Keep going and <b><marquee>learn</marquee></b> new stuff")