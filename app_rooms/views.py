from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Room

# Create your views here.

def rooms(request):
    all_rooms = Room.objects.all()
    context = { 'rooms': all_rooms }
    return render(request, 'app_rooms/rooms.html', context)

def room(request, room_id):
    one_room = None
    try:
        one_room = Room.objects.get(id=room_id)
    except:
        print('ไม่พบห้องพักนี้')
    context = { 'room': one_room }
    return render(request, 'app_rooms/room.html', context)