# Generated by Django 3.0.8 on 2020-07-12 13:10

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Başlık')),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='makale resim')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
                ('isPublished', models.BooleanField(default=True, verbose_name='yayındamı')),
                ('thisNew', models.BooleanField(default=True, verbose_name='yenimi')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar ')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='İsim')),
                ('comment_content', models.CharField(max_length=200, verbose_name='Yorum')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.Article', verbose_name='Makale')),
            ],
            options={
                'ordering': ['-comment_date'],
            },
        ),
    ]