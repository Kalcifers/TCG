import os
from django.shortcuts import render
from TCG.settings import PROJECT_ROOT


def home(request):
    return render(request, 'home.html')

def tcg(request):

    words = open(os.path.join(PROJECT_ROOT, '../static/files/prova.txt')).read()

    wordsfunz = '''[
            {text: "Muscle", weight: 15},
            {text: "Smemo", weight: 9, link: "https://www.facebook.com/matteo.ripamonti.96"},
            {text: "Power", weight: 8, html: {title: "I can haz any html attribute"}},
            {text: "Sun", weight: 7},
            {text: "Archer", weight: 6}
            ]'''
    return render(request, 'tcg.html', {'words': words, 'wordsfunz': wordsfunz})

