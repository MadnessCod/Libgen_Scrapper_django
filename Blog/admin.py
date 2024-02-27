from django.contrib import admin
from .models import ScrapperData, Title, Author, Publisher
from django.contrib.admin import register

# Register your models here.


@register(ScrapperData)
class ScrapperDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_date', 'path')
    list_display_links = ('title', 'path')
    list_filter = ('is_active', 'created_date', 'author')
    list_editable = ('is_active',)
    search_fields = ('created_date', 'author')


@ register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active', 'created_date', 'is_download')
    list_display_links = ('title',)
    list_filter = ('is_active', 'created_date',)
    list_editable = ('is_active', 'is_download',)
    search_fields = ('title', 'description',)


@register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active', 'created_date', 'is_download')
    list_display_links = ('title',)
    list_filter = ('is_active', 'created_date',)
    list_editable = ('is_active', 'is_download',)
    search_fields = ('title', 'description',)


@register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active', 'created_date', 'is_download')
    list_display_links = ('title',)
    list_filter = ('is_active', 'created_date',)
    list_editable = ('is_active', 'is_download',)
    search_fields = ('title', 'description',)
