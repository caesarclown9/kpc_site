from django.shortcuts import render, redirect, get_object_or_404


from .models import *
# from .parser import all

def index(request):
    currency = all
    news = News.objects.order_by("-created_at")[:3]
    rates = Rates.objects.latest('date')
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html', locals())


def partners(request):
    return render(request, 'partners.html', locals())


def ecology(request):
    return render(request, 'ecology.html', locals())


def news_detail(request, pk):
    post = News.objects.filter(pk=pk).first()
    return render(request, 'news_detail.html', locals())


def all_news(request):
    news = News.objects.all()
    return render(request, 'news_list.html', locals())


