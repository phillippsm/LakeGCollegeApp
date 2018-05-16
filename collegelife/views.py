from django.shortcuts import render
from django.http import HttpResponse
from .models import Clubs

def home(request):
  clubs = Clubs.objects.all()
  return render(request, 'home.html', {'clubs': clubs})

# Create your views here.
