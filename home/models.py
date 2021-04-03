from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import ModelForm,TextInput, Textarea


#_____________________ Site ayarları modeli__________
class MySetting(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )

    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length = 255)
    company = models.CharField(max_length=150)
    address = models.TextField(blank = True,max_length=150)
    phone = models.CharField(blank = True,max_length=15)
    fax = models.CharField(blank = True,max_length = 15)
    email = models.CharField(blank = True,max_length = 75)
    smtp_server = models.CharField(blank = True,max_length=20)
    smtpemail = models.CharField(blank = True,max_length=20)
    smtppassword = models.CharField(blank = True,max_length = 10)
    smtpport = models.CharField(blank = True,max_length = 5)
    icon = models.ImageField(blank = True, upload_to='images/')
    facebook = models.CharField(blank = True,max_length =100)
    instagram = models.CharField(blank = True,max_length = 100)
    twitter = models.CharField(blank = True,max_length=100)
    aboutus = RichTextUploadingField(blank = True)
    contact = RichTextUploadingField(blank = True)
    references = RichTextUploadingField(blank = True)
    status = models.CharField(max_length=10,choices=STATUS, default=True)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.title



#________________________________ İLETİŞİM MODEL _______________________________
class ContactFormMessage(models.Model):
    STATUS = (
        ('New','Yeni'),
        ('Read','Okundu'),
        ('Closed','İşleme Konuldu'),
    )

    name = models.CharField(max_length=40)
    email = models.CharField(max_length=80)
    subject = models.CharField(blank=True,max_length=50)
    message = models.TextField(max_length=255)
    status = models.CharField(max_length=25, choices=STATUS, default='New')
    ip = models.CharField(blank=True,max_length=25)
    note = models.CharField(blank=True,max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)



    def __str__(self):
        return self.name

#________________________________ İLETİŞİM Form MODELİ _______________________________

class ContactFormu(ModelForm):

    class Meta:
        model = ContactFormMessage
        fields = ['name','email','subject','message']
        widgets = {
            'name' : TextInput(attrs={'class':'input','placeholder':'İsim & Soyisim'}),
            'subject' : TextInput(attrs={'class':'input','placeholder':'Konu'}),
            'email' : TextInput(attrs={'class':'input', 'placeholder':'Email Adresiniz'}),
            'message' : Textarea(attrs={'class':'input', 'placeholder':'Your Message','style':'height:30rem;'}),

        }










