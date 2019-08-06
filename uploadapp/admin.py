# Register your models here.
from uploadapp.models import FileModel
from django.contrib import admin
from datetime import timezone, datetime

class FileAdmin( admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields':['file_origin_name']}),
        ('Date information' ,   {'fields':['file_path']})
    ]
    
    list_display = ('file_origin_name', 'file_path' , 'file_ext', 'is_img','create_date')

    def was_published_recently(self):
        return self.create_date >= timezone.now() - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = 'create_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '  '
    
    list_filter = ['create_date']
    
    search_fields = ['file_origin_name']
    
admin.site.register(FileModel, FileAdmin)