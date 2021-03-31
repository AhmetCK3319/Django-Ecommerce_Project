from django.shortcuts import render





def index(request):

    text = "My text ..."
    context = {'text':text}

    return render(request,"index.html", context=context)