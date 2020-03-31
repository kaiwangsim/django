from django.contrib import admin

# Register your models here.

from .models import base

class admin1(admin.ModelAdmin):
    list_display = ['name', 'label', 'cdate']
    readonly_fields = ['cdate']


admin.site.register(base, admin1)