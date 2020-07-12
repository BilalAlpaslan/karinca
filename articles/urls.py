from django.urls import path
from . import views





urlpatterns= [
	path('',views.index,name='articles'),
	path('<int:articles_id>',views.detail,name='detail'),
	path('comment/<int:articles_id>',views.addComment,name = "comment"),
]