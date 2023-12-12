from django.shortcuts import render, redirect
from .models import Article, Commentary
from django.http import Http404, HttpResponseNotFound


# Create your views here.


def indexpage(request):
    articles = Article.objects.all()
    return render(request, "index.html ", {"articles": articles, "page": "index"})


def aboutpage(request):
    return render(request, 'about.html', {"page": "about"})


def contactpage(request):
    if request.method == "GET":
        return render(request, "contact.html", {"page": "contact"})
    else:
        print(request.POST)
        file = open('D:/contact_results.txt', 'w')
        file.writelines(
            f"Name: {request.POST['name'].encode('utf-8', 'ignore')},Email: {request.POST['email'].encode('utf-8', 'ignore')},Subject: {request.POST['subject'].encode('utf-8', 'ignore')}")
        return redirect(contactpage)


def articlepage(request, article_id):
    article = Article.objects.filter(id=article_id).first()
    if article:
        comments = Commentary.objects.filter(Article=article).all()
        return render(request, 'article.html', {'article': article, "comments": comments})

    return Http404("Article not found")


def commentpost(request, article_id):
    if request.method == "POST":
        print(request.POST)
        article = Article.objects.filter(id=article_id).first()
        if 'name' in request.POST and 'email' in request.POST and 'message' in request.POST:
            article.new_comment(request.POST)
            return redirect(articlepage, article_id)

    return HttpResponseNotFound("404")
