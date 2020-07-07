# Generated by Django 3.0.6 on 2020-05-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_auto_20200530_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategori',
            name='text',
            field=models.CharField(default=1, max_length=100, verbose_name='kategori yazısı'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('1', 'inceleme'), ('2', 'elestiri'), ('3', 'yonetmenİnceleme'), ('4', 'oscard'), ('5', 'vizyon')], max_length=100),
        ),
    ]
