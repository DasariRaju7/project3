from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jampandu(request):
    return HttpResponse('<h1><marquee>hi jampandu how are you</h1></marquee>')