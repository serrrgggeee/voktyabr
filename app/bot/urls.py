from django.urls import  path

from bot.views import search

urlpatterns = [
    path('search_bot', search, name='search_bot')

]