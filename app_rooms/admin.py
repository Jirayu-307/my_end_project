from django.contrib import admin
from app_rooms.models import Room

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    
admin.site.register(Room, RoomAdmin)