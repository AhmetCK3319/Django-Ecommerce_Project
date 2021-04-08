from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from home.models import MySetting, ContactFormMessage, ContactFormu
from product.models import Product, Category, Images


#__________________________________ index() _______________________________________
def index(request):

    setting = MySetting.objects.get()
    sliderdata = Product.objects.all()[:4] #Tüm Product'ları getirme, bana 4 tanesini getir.
    category = Category.objects.all()
    dayproducts = Product.objects.all()[:12] # Günün ürünleri
    lastproducts = Product.objects.all().order_by("-id")[:4] # Son ürünler
    randomproducts = Product.objects.all().order_by("?")[:4] # Rastgele ürünler




    context = {
        'setting':setting,
        'page':'home',
        'sliderdata':sliderdata,
        'category':category,
        'dayproducts':dayproducts,
        'lastproducts':lastproducts,
        'randomproducts':randomproducts,

    }

    return render(request,"index.html", context=context)


#__________________________________ hakkimizda() _______________________________________
def hakkimizda(request):
    setting = MySetting.objects.get()
    context = {
        'setting':setting,

    }

    return render(request,"hakkimizda.html", context)

#__________________________________ referanslar() _______________________________________
def referanslar(request):
    setting = MySetting.objects.get()
    context = {
        'setting':setting,

    }

    return render(request,"referanslar.html", context)


#__________________________________ iletisim() _______________________________________
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


def category_products(request,id,slug):
        category = Category.objects.all()
        category_data =Category.objects.get(pk=id)
        products = Product.objects.filter(category_id = id)
        context = {
            'products':products,
            'category':category,
            'category_data':category_data,
        }

        return render(request,"products.html",context=context)


def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    context = {
        'product':product,
        'category':category,
        'images':images,
    }

    return render(request,"product_detail.html",context=context)

