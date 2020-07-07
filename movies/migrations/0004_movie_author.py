# Generated by Django 3.0.6 on 2020-05-17 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_movie_yonetmen'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar '),
            preserve_default=False,
        ),
    ]
