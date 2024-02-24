from django.contrib import admin
from .models import ScrapperData
from django.contrib.admin import register

# Register your models here.


@register(ScrapperData)
class ScrapperDataAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'is_active', 'created_date', 'updated_date', 'path')
    list_display_links = ('number', 'title', 'path')
    list_filter = ('is_active', 'created_date', 'updated_date', 'title', 'author')
    list_editable = ('is_active',)
    search_fields = ('title', 'author')
