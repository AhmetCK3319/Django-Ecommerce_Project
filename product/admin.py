from django.contrib import admin

from product.models import Category,Product,Images


class ProductImageInline(admin.TabularInline):
        model = Images
        extra = 5



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        search_fields = ['title', 'description', 'keywords']
        readonly_fields = ('my_image_tag',)
        list_display=['title','status','my_image_tag']
        list_filter=['status','create_at']



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
        list_display = ['title','category','price','amount','image_tag','status']
        list_filter = ['status','create_at','category']
        search_fields = ['title','category','price','keywords']
        inlines = [ProductImageInline]
        readonly_fields = ('image_tag',)


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
        list_display=['title','my_image_tag','product']
        list_display_links = ['title','my_image_tag','product']
        readonly_fields = ('my_image_tag',)
        search_fields = ['title','product']



