from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar ")
    name = models.CharField(max_length=100, verbose_name='Başlık')
    description = RichTextField()
    image = models.FileField(blank = True,null = True, verbose_name='makale resim')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')
    isPublished = models.BooleanField(default= True, verbose_name='yayındamı') 
    thisNew = models.BooleanField(default= True, verbose_name='yenimi')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
        

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
        

