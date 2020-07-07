from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie
from .models import Duyuru,AboutP


def index(request):
    keyword = request.GET.get("keyword")
    if keyword:
        movies = Movie.objects.all().filter(isPublished = 1).filter(name__contains = keyword)

        context = {
        'movies': movies
        }
        return render(request,'movies/list.html', context)

    else:
        movies = Movie.objects.filter(isPublished = 1).filter( thisNew = 1 )
        duyuru = Duyuru.objects.filter(isPublished = 1).filter( thisNew = 1 )
 
        context = {
            'movies': movies ,
            'duyuru': duyuru
        }
    
        return render(request, 'pages/index.html', context)


def about(request):
    aboutP = AboutP.objects.filter( id = 1 )
    context = {
        'aboutP' : aboutP
    }

    return render(request, 'pages/about.html', context)



