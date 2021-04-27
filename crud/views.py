from django.shortcuts import render, redirect, get_object_or_404

from .models import *

def index(request):
    news = News.objects.all()
    return render(request, 'index.html', locals())

