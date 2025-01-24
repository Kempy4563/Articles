from django.shortcuts import render
from django.http import HttpResponse
from app.models import Article, UserProfile


def home(request):
    articles = Article.objects.all()
    print(articles)
    return render(request, 'app/home.html', {'articles': articles})
