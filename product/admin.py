from django.contrib import admin

from product.models import Category,Product



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        search_fields = ['title', 'description', 'keywords']
        list_display=['title','status']
        list_filter=['status','create_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
        list_display = ['title','category','price','amount','status']
        list_filter = ['status','create_at','category']
        search_fields = ['title','category','price','keywords']