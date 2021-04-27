from django.urls import path

from .views import *

app_name = 'crud'

urlpatterns = [
    path('', index, name='index')
]