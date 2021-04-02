from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include




urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/',include('home.urls')),
    path('product/', include('product.urls')),


]

#_______________ ADMIN'DE Image Görsellik..
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)