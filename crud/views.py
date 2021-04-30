from django.shortcuts import render, redirect, get_object_or_404


from .models import *
# from .parser import all

def index(request):
    currency = all
    news = News.objects.all()
    rates = Rates.objects.latest('date')
    return render(request, 'index.html', locals())



