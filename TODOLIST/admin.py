from django.contrib import admin
from .models import todo1
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class peopleres (resources.ModelResource):
    class Meta:
        model = todo1
        skip_unchanged = True
        report_skipped  = False

class deviceadmin(ImportExportModelAdmin):
    resource_class = peopleres
    list_display = ['name', 'cdate', 'status1']
    list_filter = ['cdate', '状态']
    search_fields = ['name']

admin.site.register(todo1, deviceadmin)
