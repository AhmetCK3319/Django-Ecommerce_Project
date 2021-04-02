from django.contrib import admin

from product.models import Category,Product,Images


class ProductImageInline(admin.TabularInline):
        model = Images
        extra = 5



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
        inlines = [ProductImageInline]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
        list_display=['title','product','image']
        search_fields = ['title','product']
        list_display_links=['title','product']