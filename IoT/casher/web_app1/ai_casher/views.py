from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'ai_casher/index.html', {})

def room(request, room_name):
    return render(request, 'ai_casher/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })