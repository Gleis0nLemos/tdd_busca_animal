from django.contrib import admin
from django.urls import path
from animals.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
]
