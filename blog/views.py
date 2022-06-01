from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def category(request):
    if request.method == 'GET':
        category_list = Category.objects.all()

        category_count = {}

        for category in category_list:
            name = category.name
            count = len(Article.objects.filter(category=category))
            category_count[name] = count

        return render(request, 'category.html', {'category_count': category_count})

def new(request):
    if request.method == 'POST':
        my_article = Article()
        my_article.title = request.POST.get('title')
        my_article.content = request.POST.get('content')
        category = request.POST.get('category')
        my_article.category = Category.objects.get(name=category)
        my_article.save()

        return redirect('/')

    elif request.method == 'GET':
        category_list = Category.objects.all()
        return render(request, 'new.html', {'category_list': category_list})

def article(request, name):
    category = Category.objects.get(name=name)
    articles = Article.objects.filter(category=category)
    return render(request, 'article.html', {'articles': articles})


def detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'detail.html', {'article': article})






