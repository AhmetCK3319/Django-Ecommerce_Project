from django.shortcuts import render

from home.models import MySetting


def index(request):

    setting = MySetting.objects.get()

    context = {
        'setting':setting,
        'page':'home',
    }

    return render(request,"index.html", context)

def hakkimizda(request):
    setting = MySetting.objects.get()
    context = {
        'setting':setting,

    }

    return render(request,"hakkimizda.html", context)


def referanslar(request):
    setting = MySetting.objects.get()
    context = {
        'setting':setting,

    }

    return render(request,"referanslar.html", context)


def iletisim(request):
    setting = MySetting.objects.get()
    context = {
        'setting':setting,

    }

    return render(request,"iletisim.html", context)