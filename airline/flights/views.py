from django.shortcuts import render
from .models import Flight

# Create your views here.
def index():
    return render(request, "flights/index.html",{
        "flights" : Flight.objects.all()
    })
