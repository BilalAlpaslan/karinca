from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Articles
from .models import Duyuru,AboutP


def index(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Articles.objects.all().filter(isPublished = 1).filter(name__contains = keyword)

        context = {
        'articles': articles
        }
        return render(request,'articles/list.html', context)

    else:
        articles = Articles.objects.filter(isPublished = 1).filter( thisNew = 1 )
        duyuru = Duyuru.objects.filter(isPublished = 1).filter( thisNew = 1 )
 
        context = {
            'articles': articles ,
            'duyuru': duyuru
        }
    
        return render(request, 'pages/index.html', context)


def about(request):
    aboutP = AboutP.objects.filter( id = 1 )
    context = {
        'aboutP' : aboutP
    }

    return render(request, 'pages/about.html', context)



