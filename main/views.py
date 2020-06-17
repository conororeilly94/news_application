from django.shortcuts import render, get_object_or_404, redirect
from .models import Main

# Create your views here. ACTIONS


def home(request):


    return render(request, 'home.html')