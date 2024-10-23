from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('<h1>เกสต์เฮาส์บุปผาธารา</h1>')

def about(request):
    return HttpResponse('เกี่ยวกับเกสต์เฮาส์บุปผาธารา')