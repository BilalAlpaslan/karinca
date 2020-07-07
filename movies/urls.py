from django.urls import path
from . import views





urlpatterns= [
	path('',views.index,name='movies'),
	path('filtre/<int:kategori_id>',views.filtre,name='filtre'),
	path('<int:movie_id>',views.detail,name='detail'),
	path('comment/<int:movie_id>',views.addComment,name = "comment"),
]