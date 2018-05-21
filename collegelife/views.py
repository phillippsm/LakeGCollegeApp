from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Clubs

@login_required
def home(request):
  clubs = Clubs.objects.all()
  return render(request, 'home.html', {'clubs': clubs})

# Create your views here.
