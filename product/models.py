from django.db import models
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import  RichTextUploadingField


#_________________________________ Category(models.Model)_________________________________________

class Category(models.Model):

    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True,null=True, related_name='children',on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add =True)
    update_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.title

    # Admin panelde Image gösterimi
    def my_image_tag(self):

        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""

    my_image_tag.short_description = 'Image'

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
    slug = models.SlugField(editable=False)
    status = models.CharField(max_length = 10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)


    #Admin panelde Image gösterimi
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""

    image_tag.short_description = 'Image'


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















