from django.urls import path
from django.urls.resolvers import URLPattern
from .views import index,show_articles,timetable

urlpatterns = [
    path('',index),
    path('articles/',show_articles,name='articles'),
    path('timetable/',timetable),
]