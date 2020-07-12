from django.shortcuts import render,get_object_or_404,reverse,redirect,HttpResponse
from django.contrib.auth.decorators import login_required  
from django.http import Http404
from .models import Article,Comment
from django.contrib.auth.models import User
from django.contrib import auth


def index(request):
    keyword = request.GET.get("keyword")
    kategori = Kategori.objects.all()

    if keyword:
        articles = Article.objects.all().filter(isPublished = 1).filter(name__contains = keyword)

        context = {
        'articles': articles,
        'kategori': kategori
        }
        return render(request,'articles/list.html', context)

    else:
        articles = Article.objects.all().filter(isPublished = 1)

        context = {
            'articles': articles,
            'kategori': kategori
        }
        return render(request, 'articles/list.html', context)


def detail(request, articles_id):
    articles = get_object_or_404(Article, pk = articles_id)
    comments = articles.comments.all()
    context = {
        'articles': articles,
        "comments":comments
    }
    return render(request, 'articles/detail.html', context)



@login_required(login_url = "login")
def addComment(request,articles_id):
    articles = get_object_or_404(Article, pk = articles_id)

    if request.method == "POST":
        comment_author = request.user.username
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)
        newComment.articles = articles
        newComment.save()

    return redirect(reverse("detail",kwargs={"articles_id":articles_id}))
    
