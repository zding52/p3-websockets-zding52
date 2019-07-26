from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})
  
def one(request):
    return render(request, 'draw/1.html')
  
def two(request):
    return render(request, 'draw/2.html')
  
def three(request):
    return render(request, 'draw/3.html')
  
def four(request):
  return render(request, 'draw/4.html')

def five(request):
  return render(request, 'draw/5.html')

def six(request):
    return render(request, 'draw/6.html')
  