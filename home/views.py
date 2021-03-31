from django.shortcuts import render





def index(request):

    text = "My text ... <br>Ugur hmz <strong>Burası BOSTON/MA</strong>"
    context = {'text':text}

    return render(request,"index.html", context=context)