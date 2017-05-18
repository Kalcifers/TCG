from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def tcg(request):
    return render(request, 'tcg.html')