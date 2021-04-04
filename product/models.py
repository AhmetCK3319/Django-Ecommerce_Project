from django.db import models
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import  RichTextUploadingField

from mptt.models import MPTTModel, TreeForeignKey

#_________________________________ Category(models.Model)_________________________________________

class Category(MPTTModel):

    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(max_length=130,unique=True,editable=False)
    parent = TreeForeignKey('self',blank=True,null=True, related_name='children',on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add =True)
    update_at = models.DateField(auto_now=True)

    #Category -> Ağaç yapısı için
    class MPTTMeta:
       # level_attr ='mptt_level'
        order_insertion_by = ['title']




    #iç içe Kategori Gösterimi
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent

        return ' / '.join(full_path[::-1])


    # Admin panelde Image gösterimi
    def my_image_tag(self):

        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""

    my_image_tag.short_description = 'Image'

    # slug'da ı'ları i yapma
    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, counter)
            counter += 1
        return unique_slug

    # slug'ı kaydetme
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Category, self).save(*args, **kwargs)






#_________________________________ Product(models.Model)_________________________________________

class Product(models.Model):

    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail =RichTextUploadingField()
    slug = models.SlugField(max_length=130,unique =True,editable=False)
    status = models.CharField(max_length = 10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.title





    #Admin panelde Image gösterimi
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""

    image_tag.short_description = 'Image'



    #slug'da ı'ları i yapma
    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, counter)
            counter += 1
        return unique_slug


    #slug'ı kaydetme
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Product, self).save(*args, **kwargs)






#_________________________________ Images(models.Model)_________________________________________

class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')



    def __str__(self):
        return self.title

    # Admin panelde Image gösterimi
    def my_image_tag(self):

        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""

    my_image_tag.short_description = 'Image'















