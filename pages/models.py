from django.db import models
from ckeditor.fields import RichTextField

class Duyuru(models.Model):
    baslik = models.CharField(max_length=100, verbose_name='Duyuru Başlığı')
    icerik = RichTextField()
    image = models.FileField(blank = True,null = True, verbose_name='Resim')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')
    isPublished = models.BooleanField(default= True, verbose_name='yayındamı') 
    thisNew = models.BooleanField(default= True, verbose_name='yenimi')

    def __str__(self):
        return self.baslik

class AboutP(models.Model):
    baslik = models.CharField(max_length=100, verbose_name='hakkımızda s. başlığı')
    icerik = RichTextField()

    def __str__(self):
        return self.baslik

