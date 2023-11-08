from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<marquee><h1>Hi everone Creating the DJango Project</h1></marquee>")