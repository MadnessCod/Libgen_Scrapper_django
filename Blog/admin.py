from django.contrib import admin
from django.contrib.admin import register

from import_export.admin import ImportExportModelAdmin

from .models import Author, Publisher, Year, Language, Extension, Book


# Register your models here.


@register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = (
        'title',
        'author',
        'publisher',
        'year',
        'type',
        'language',
        'created_date',
        'is_download',
        'is_active',
    )
    list_display_links = ('title', 'language', 'year')
    list_filter = ('year', 'language', 'type')
    list_editable = ('is_active', 'is_download')
    search_fields = ('created_date', 'author')


@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_active', 'is_download')
    list_display_links = ('title', 'created_date',)
    list_filter = ('is_active', 'created_date',)
    list_editable = ('is_active', 'is_download',)
    search_fields = ('title',)


@register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_active', 'is_download')
    list_display_links = ('title', 'created_date')
    list_filter = ('is_active', 'created_date',)
    list_editable = ('is_active', 'is_download',)
    search_fields = ('title',)


@register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_active', 'is_download')
    list_display_links = ('title',)
    list_filter = ('is_active', 'created_date',)
    list_editable = ('is_active', 'is_download',)
    search_fields = ('title',)


@register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_active', 'is_download')
    list_display_links = ('title',)
    list_filter = ('is_active', 'created_date',)
    list_editable = ('is_active', 'is_download',)
    search_fields = ('title',)


@register(Extension)
class ExtensionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_active', 'is_download')
    list_display_links = ('title', 'created_date')
    list_filter = ('is_active', 'created_date',)
    list_editable = ('is_active', 'is_download',)
    search_fields = ('title',)
