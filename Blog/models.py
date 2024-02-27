from django.db import models


class MyBaseClass(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='is active')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    is_download = models.BooleanField(default=False, verbose_name='is download')

    class Meta:
        abstract = True
        ordering = ('pk',)


class Author(MyBaseClass):
    title = models.CharField(max_length=100, null=False, verbose_name='Title')
    description = models.TextField(null=False, blank=False, verbose_name='Description')

    class Meta:
        verbose_name = 'author'

    def __str__(self):
        return self.title


class Title(MyBaseClass):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Title')
    description = models.TextField(null=False, blank=False, verbose_name='Description')

    class Meta:
        verbose_name = 'Title'

    def __str__(self):
        return self.title


class Publisher(MyBaseClass):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Publisher')
    description = models.TextField(null=False, blank=False, verbose_name='Description')

    class Meta:
        verbose_name = 'Publisher'

    def __str__(self):
        return self.title


class ScrapperData(MyBaseClass):
    number = models.CharField(max_length=10, null=False)
    author = models.ForeignKey(
        Author,
        null=False,
        on_delete=models.PROTECT,
        verbose_name='Author'
    )
    title = models.ForeignKey(
        Title,
        null=False,
        on_delete=models.PROTECT,
        verbose_name='Title'
    )
    publisher = models.ForeignKey(
        Publisher,
        null=False,
        on_delete=models.PROTECT,
        verbose_name='Publisher'
    )
    year = models.CharField(max_length=10)
    page = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    path = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Book'
