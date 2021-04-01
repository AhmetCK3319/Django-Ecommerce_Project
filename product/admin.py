from django.contrib import admin

from product.models import Category



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        list_display=['title','status']
        list_filter=['status','create_at']
