# mysite/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^ai_casher/', include('ai_casher.urls')),
    url(r'^admin/', admin.site.urls),
]