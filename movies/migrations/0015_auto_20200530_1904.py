# Generated by Django 3.0.6 on 2020-05-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('inceleme', 'inceleme'), ('elestiri', 'elestiri'), ('yonetmenİnceleme', 'yonetmenİnceleme'), ('oscard', 'oscard'), ('vizyon', 'vizyon')], max_length=100),
        ),
    ]
