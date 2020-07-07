from django.shortcuts import render,get_object_or_404,reverse,redirect,HttpResponse
from django.contrib.auth.decorators import login_required  
from django.http import Http404
from .models import Movie,Comment,Kategori
from django.contrib.auth.models import User
from django.contrib import auth


def index(request):
    keyword = request.GET.get("keyword")
    kategori = Kategori.objects.all()

    if keyword:
        movies = Movie.objects.all().filter(isPublished = 1).filter(name__contains = keyword)

        context = {
        'movies': movies,
        'kategori': kategori
        }
        return render(request,'movies/list.html', context)

    else:
        movies = Movie.objects.all().filter(isPublished = 1)

        context = {
            'movies': movies,
            'kategori': kategori
        }
        return render(request, 'movies/list.html', context)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk = movie_id)
    comments = movie.comments.all()
    context = {
        'movie': movie,
        "comments":comments
    }
    return render(request, 'movies/detail.html', context)



@login_required(login_url = "login")
def addComment(request,movie_id):
    movie = get_object_or_404(Movie, pk = movie_id)

    if request.method == "POST":
        comment_author = request.user.username
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)
        newComment.movie = movie
        newComment.save()

    return redirect(reverse("detail",kwargs={"movie_id":movie_id}))
    

def filtre(request,kategori_id):
    movies = Movie.objects.all().filter(isPublished = 1).filter(category = kategori_id)
    context = {
        'movies': movies
    }
    return render(request, 'movies/filtre.html', context)