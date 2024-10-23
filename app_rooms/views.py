from django.http.response import HttpResponse
from django.shortcuts import render

all_rooms = [
    {'id': 1, 'title': 'ห้องพักหมายเลข 1', 'price': 699, 'is_multiple_bed': True},
    {'id': 2, 'title': 'ห้องพักหมายเลข 2', 'price': 499, 'is_multiple_bed': False},
    {'id': 3, 'title': 'ห้องพักหมายเลข 3', 'price': 699, 'is_multiple_bed': True},
    {'id': 4, 'title': 'ห้องพักหมายเลข 4', 'price': 499, 'is_multiple_bed': False},
]

# Create your views here.

def rooms(request):
    context = { 'rooms': all_rooms }
    return render(request, 'app_rooms/rooms.html', context)

def room(request, room_id):
    one_room = None
    try:
        one_room = [r for r in all_rooms if r['id'] == room_id][0]
    except IndexError:
        print('ไม่พบห้องพักนี้')
    context = { 'room': one_room }
    return render(request, 'app_rooms/room.html', context)