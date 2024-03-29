# Generated by Django 4.2 on 2024-03-16 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_author_publisher_title_alter_scrapperdata_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('is_download', models.BooleanField(default=False, verbose_name='is download')),
                ('size', models.CharField(max_length=50, verbose_name='size')),
                ('number', models.CharField(max_length=10, verbose_name='number')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('page', models.CharField(max_length=50, verbose_name='page')),
                ('path', models.CharField(max_length=200, verbose_name='path')),
            ],
            options={
                'verbose_name': 'Book',
            },
        ),
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('is_download', models.BooleanField(default=False, verbose_name='is download')),
                ('title', models.CharField(max_length=100, verbose_name='extension')),
            ],
            options={
                'verbose_name': 'Extension',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('is_download', models.BooleanField(default=False, verbose_name='is download')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Language',
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('is_download', models.BooleanField(default=False, verbose_name='is download')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Year',
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': 'Publisher', 'verbose_name_plural': 'Publishers'},
        ),
        migrations.RemoveField(
            model_name='author',
            name='description',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='description',
        ),
        migrations.AlterField(
            model_name='author',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
        migrations.DeleteModel(
            name='ScrapperData',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Blog.author', verbose_name='author'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Blog.language', verbose_name='language'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Blog.publisher', verbose_name='publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Blog.extension', verbose_name='type'),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Blog.year', verbose_name='year'),
        ),
    ]
