from django.contrib import admin
from mptt.admin import  DraggableMPTTAdmin
from product.models import Category, Product, Images, Comment




#_____________________________ CategoryAdmin_______________________________
class ProductImageInline(admin.TabularInline):
        model = Images
        extra = 5



#_____________________________ CategoryAdmin_______________________________
class CategoryAdmin(admin.ModelAdmin):
        search_fields = ['title', 'description', 'keywords']
        readonly_fields = ('my_image_tag',)
        list_display=['title','status','my_image_tag']
        list_filter=['status','create_at']


#_____________________________ ProductAdmin_______________________________
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
        list_display = ['title','category','price','amount','image_tag','status','slug']
        list_filter = ['status','create_at','category']
        search_fields = ['title','category','price','keywords']
        inlines = [ProductImageInline]
        readonly_fields = ('image_tag',)



#_____________________________ ImagesAdmin________________________________
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
        list_display=['title','my_image_tag','product']
        list_display_links = ['title','my_image_tag','product']
        readonly_fields = ('my_image_tag',)
        search_fields = ['title','product']


#_____________________________ CategoryAdmin2________________________________
class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


admin.site.register(Category,CategoryAdmin2)

#_____________________________ CommentAdmin________________________________
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','product','user','status']
    list_filter = ['status']












