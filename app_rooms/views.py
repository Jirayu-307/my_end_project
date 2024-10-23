from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def rooms(request):
    return HttpResponse('ห้องพักทั้งหมด')

def room(request, room_id):
    return HttpResponse('ห้องนี้หมายเลข = ' + str(room_id))