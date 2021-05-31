from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import FileResponse
import os
from django.conf import settings
from .models import Product
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# ListView
class BoardLV(ListView):
    model = Product
    template_name = 'show.html'   # 템플릿 파일명 변경
    context_object_name = 'product_list'          # 컨텍스트 객체 이름 변경(object_list)

def index(request):
    return render(request, 'show.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
    
def erase_list(request):
    pass