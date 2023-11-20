from django.shortcuts import render

# Create your views here.

def bahubali(request):
    return render(request,'bahubali.html')

def kattapa(request):
    return render(request,'kattapa.html')

def devasena(request):
    return render(request,'devasena.html')