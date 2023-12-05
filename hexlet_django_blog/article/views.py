from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm
from django.db.models import Q


class IndexView(View):

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        articles = Article.objects.filter(Q(name__icontains=query))
        return render(request, 'articles/index.html', context={
            'articles': articles, 'search': query
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/article.html',
            context={'article': article}
        )


class ArticleFormCreateView(View):
    __template = 'articles/create.html'

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, self.__template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles_index')
        return render(request, self.__template, {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request,
            'articles/update.html',
            {'form': form, 'article_id': article_id}
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles_index')
        return render(
            request,
            'articles/update.html',
            {'form': form, 'article_id': article_id}
        )


class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles_index')
