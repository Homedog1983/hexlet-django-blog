from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm
from django.db.models import Q

# Идея для развития: приложение .comments - модель: одна статья - много комментов.
# Связь через foreignKey (id_статьи). Если статья удаляется - все комменты, привязанные
# к ней - тоже. Вью: гет(статья + индекс комментов+форма коммента заполненная с эррорс),
# пост: передача с редиректом на гет с новым комментом. Сортировка - последние комменты вверху.


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
