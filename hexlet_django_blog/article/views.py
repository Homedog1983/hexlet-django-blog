from django.shortcuts import render
from django.views import View
from hexlet_django_blog.article.models import Article


class IndexView(View):
    tags = ['Учебный проект', 'фреймворк Django (Python)', 'Статьи']
    template = 'articles/index.html'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class TagsIdView(View):
    template = 'articles/article.html'

    def get(self, request, tags: str, article_id: int, *args, **kwargs):
        return render(
            request,
            self.template,
            context={'tags': tags, 'article_id': article_id},
        )
