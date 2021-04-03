from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('hakkimizda/',views.hakkimizda, name='hakkimizda'),
    path('referanslar/',views.referanslar, name='referanslar'),
    path('iletisim/',views.iletisim, name='iletisim'),
    path('home/',include('home.urls')),
    path('product/', include('product.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

#_______________ ADMIN'DE Image Görsellik..
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)