from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from home.models import MySetting, ContactFormMessage, ContactFormu


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

    if request.method=='POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR') #Client ip alma
            data.save()
            messages.success(request,"Mesajınız başarılı bir şekilde gönderilmiştir. Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')



    setting = MySetting.objects.get()
    form = ContactFormu()
    context = {
        'setting':setting,
        'form':form,
    }

    return render(request,"iletisim.html", context=context)


