from django.contrib import admin
from .models import Article,Comment



admin.site.register(Comment)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','name',"author",'created_date','isPublished',"thisNew")
    list_display_links = ('id','name')
    list_filter = ('created_date',)
    list_editable = ('isPublished',"thisNew")
    search_fields = ('name','description')
    list_per_page = 20
admin.site.register(Article, ArticleAdmin)


