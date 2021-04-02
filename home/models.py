from django.db import models




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
    aboutus = models.TextField(blank = True,)
    contact = models.TextField(blank = True,)
    references = models.TextField(blank = True,)
    status = models.CharField(max_length=10,choices=STATUS, default=True)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.title
