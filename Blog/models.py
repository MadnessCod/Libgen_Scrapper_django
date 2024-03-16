from django.db import models


class MyBaseModel(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='is active')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    is_download = models.BooleanField(default=False, verbose_name='is download')

    class Meta:
        abstract = True
        ordering = ('pk',)


class Author(MyBaseModel):
    title = models.CharField(max_length=100, null=False, verbose_name='title')

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.title


class Publisher(MyBaseModel):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Publisher')

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return self.title


class Year(MyBaseModel):
    title = models.CharField(max_length=100, verbose_name='title')

    class Meta:
        verbose_name = 'Year'

    def __str__(self):
        return self.title


class Language(MyBaseModel):
    title = models.CharField(max_length=100, verbose_name='title')

    class Meta:
        verbose_name = 'Language'

    def __str__(self):
        return self.title


class Extension(MyBaseModel):
    title = models.CharField(max_length=100, verbose_name='extension')

    class Meta:
        verbose_name = 'Extension'

    def __str__(self):
        return self.title


class Book(MyBaseModel):
    author = models.ForeignKey(
        Author,
        null=False,
        on_delete=models.PROTECT,
        verbose_name='author'
    )
    publisher = models.ForeignKey(
        Publisher,
        null=False,
        on_delete=models.PROTECT,
        verbose_name='publisher'
    )
    year = models.ForeignKey(
        Year,
        on_delete=models.PROTECT,
        verbose_name='year'
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.PROTECT,
        verbose_name='language',
    )
    type = models.ForeignKey(
        Extension,
        on_delete=models.PROTECT,
        verbose_name='type',
    )
    size = models.CharField(max_length=50, verbose_name='size')
    number = models.CharField(max_length=10, null=False, verbose_name='number')
    title = models.CharField(max_length=200, verbose_name='title')
    page = models.CharField(max_length=50, verbose_name='page')
    path = models.CharField(max_length=200, verbose_name='path')

    class Meta:
        verbose_name = 'Book'
