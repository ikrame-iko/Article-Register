from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.


def article_list(request):
    context = {'article_list': Article.objects.all()}
    return render(request, "article_register/article_list.html", context)


def article_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ArticleForm()
        else:
            article = Article.objects.get(pk=id)
            form = ArticleForm(instance=article)
        return render(request, "article_register/article_form.html", {'form': form})
    else:
        if id == 0:
            form = ArticleForm(request.POST)
        else:
            article = Article.objects.get(pk=id)
            form = ArticleForm(request.POST,instance= article)
        if form.is_valid():
            form.save()
        return redirect('/article/list')


def article_delete(request,id):
    article = Article.objects.get(pk=id)
    article.delete()
    return redirect('/article/list')