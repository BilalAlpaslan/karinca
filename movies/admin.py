from django.contrib import admin
from .models import Movie,Comment,Kategori



admin.site.register(Comment)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','name',"author",'created_date','isPublished',"thisNew")
    list_display_links = ('id','name')
    list_filter = ('created_date',)
    list_editable = ('isPublished',"thisNew")
    search_fields = ('name','description')
    list_per_page = 20
admin.site.register(Movie, MovieAdmin)



class KategoriAdmin(admin.ModelAdmin):
	list_display = ('id','name','text')
	list_display_links = ('id','name')
admin.site.register(Kategori, KategoriAdmin)