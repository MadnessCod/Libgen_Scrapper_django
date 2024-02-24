from django.db import models


class MyBaseClass(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='is active')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated date')
    is_download = models.BooleanField(default=False, verbose_name='is download')

    class Meta:
        abstract = True
        ordering = ('pk', )


class ScrapperData(MyBaseClass):
    number = models.CharField(max_length=10, null=False)
    author = models.CharField(max_length=200, null=False)
    title = models.CharField(max_length=200, null=False)
    publisher = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    page = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    path = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Libgen scrapper'
