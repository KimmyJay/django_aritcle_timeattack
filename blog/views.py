from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def main(request):
    return render(request, 'category.html')

def new(request):
    if request.method == 'POST':
        my_article = Article()
        my_article.title = request.POST.get('title', '')
        my_article.content = request.POST.get('content', '')
        my_article.category = request.POST.get('categories', '')
        my_article.save()
        return redirect('/detail')

def detail(request, id):
    if request.method == 'GET':
        article_list = Article.objects.filter(category_id=id)
        return render(request, 'user/user_list.html', {'article_list': article_list})



