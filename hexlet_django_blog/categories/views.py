from django.shortcuts import render, get_object_or_404
from django.views import View
from hexlet_django_blog.categories.models import Category


class IndexView(View):
    template = 'categories/index.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()[:15]
        return render(
            request, self.template,
            context={'categories': categories}
        )


class CategoryView(View):

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs['id'])
        articles = category.article_set.all()
        return render(
            request,
            'categories/category.html',
            context={
                'category': category,
                'articles': articles
            }
        )
