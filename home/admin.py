from django.contrib import admin

from home.models import MySetting


@admin.register(MySetting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title']
