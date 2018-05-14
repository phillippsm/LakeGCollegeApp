from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('This is College Life!')

# Create your views here.
