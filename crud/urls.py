from django.urls import path

from .views import *

app_name = 'crud'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('partners/', partners, name='partners'),
    path('ecology/', ecology, name='ecology'),
    path('news/', all_news, name='all_news'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('leaders/', all_leaders, name='all_leaders'),
    path('leaders/<int:pk>/', leader_detail, name='leader_detail'),
    path('partners/<int:pk>/', TableView.as_view(), name='tables')
]