# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1/',views.one, name='1'),
    path('2/',views.two, name='2'),
    path('3/',views.three, name='3'),
    path('4/',views.four, name='4'),
    path('5/',views.five, name='5'),
    path('6/',views.six, name='6'),
]

