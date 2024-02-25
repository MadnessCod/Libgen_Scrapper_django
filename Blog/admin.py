from django.contrib import admin
from .models import ScrapperData
from django.contrib.admin import register

# Register your models here.


@register(ScrapperData)
class ScrapperDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_date', 'path')
    list_display_links = ('title', 'path')
    list_filter = ('is_active', 'created_date', 'author')
    list_editable = ('is_active',)
    search_fields = ('created_date', 'author')
