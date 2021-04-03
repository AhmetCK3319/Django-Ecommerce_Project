from django.contrib import admin

from home.models import MySetting,ContactFormMessage


@admin.register(MySetting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields=['title','description','company','email']




@admin.register(ContactFormMessage)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','status','note']
    list_filter = ['status']
    search_fields = ['name', 'email', 'subject', 'note']