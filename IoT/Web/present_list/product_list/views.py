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
    context_object_name = 'show'          # 컨텍스트 객체 이름 변경(object_list)
    paginate_by = 20                        # 페이지네이션, 페이지 당 문서 건 수

# DetailView
class BoardDV(DetailView):
    model = Product

class BoardDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('board:index')

