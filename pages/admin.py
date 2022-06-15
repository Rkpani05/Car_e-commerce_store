from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="20" style="border-radius:50px;"/>'.format(object.photo.url))
    list_display= ['id','thumbnail','first_name','designation','created_date'] 
    
    
admin.site.register(Team,TeamAdmin)