from django.urls import path
from . import views

app_name = 'product_list'

urlpatterns = [
    path('', views.BoardLV.as_view(), name='show'),
]