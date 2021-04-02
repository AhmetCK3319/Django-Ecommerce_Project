from django.shortcuts import render

from home.models import MySetting


def index(request):

    setting = MySetting.objects.get()
    text='wqeq'
    context = {
        'setting':setting,
        'text':text
    }

    return render(request,"index.html", context)