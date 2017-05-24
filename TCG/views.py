import os
from django.shortcuts import render
from TCG.settings import PROJECT_ROOT


def home(request):
    return render(request, 'home.html')

def tcg(request):

    words = open(os.path.join(PROJECT_ROOT, '../static/files/Ready4Django.txt')).read()
    return render(request, 'tcg.html', {'words': words})

