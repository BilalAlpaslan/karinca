from django.contrib import admin
from .models import Duyuru,AboutP


class DuyuruAdmin(admin.ModelAdmin):
    list_display = ('id','baslik',"icerik",'created_date','isPublished',"thisNew")
    list_display_links = ('id','baslik')
    list_filter = ('created_date',)
    list_editable = ('isPublished',"thisNew")
    search_fields = ('baslik','icerik')
    list_per_page = 20

admin.site.register(Duyuru, DuyuruAdmin)




class AboutPAdmin(admin.ModelAdmin):
    list_display = ('id','baslik',"icerik")
    list_display_links = ('id','baslik')
    search_fields = ('baslik','icerik')
    list_per_page = 4

admin.site.register(AboutP, AboutPAdmin)