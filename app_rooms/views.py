from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def rooms(request):
    return render(request, 'app_rooms/rooms.html')

def room(request, room_id):
    return render(request, 'app_rooms/room.html', context={ 'room_id': room_id })