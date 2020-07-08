from django.shortcuts import render,get_object_or_404,reverse,redirect,HttpResponse
from django.contrib.auth.decorators import login_required  
from django.http import Http404
from .models import Articles,Comment,Kategori
from django.contrib.auth.models import User
from django.contrib import auth


def index(request):
    keyword = request.GET.get("keyword")
    kategori = Kategori.objects.all()

    if keyword:
        articles = Articles.objects.all().filter(isPublished = 1).filter(name__contains = keyword)

        context = {
        'articles': articles,
        'kategori': kategori
        }
        return render(request,'articles/list.html', context)

    else:
        articles = Articles.objects.all().filter(isPublished = 1)

        context = {
            'articles': articles,
            'kategori': kategori
        }
        return render(request, 'articles/list.html', context)


def detail(request, movie_id):
    articles = get_object_or_404(Articles, pk = movie_id)
    comments = articles.comments.all()
    context = {
        'articles': articles,
        "comments":comments
    }
    return render(request, 'articles/detail.html', context)



@login_required(login_url = "login")
def addComment(request,movie_id):
    articles = get_object_or_404(Articles, pk = movie_id)

    if request.method == "POST":
        comment_author = request.user.username
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)
        newComment.articles = articles
        newComment.save()

    return redirect(reverse("detail",kwargs={"movie_id":movie_id}))
    

def filtre(request,kategori_id):
    articles = Articles.objects.all().filter(isPublished = 1).filter(category = kategori_id)
    context = {
        'articles': articles
    }
    return render(request, 'articles/filtre.html', context)