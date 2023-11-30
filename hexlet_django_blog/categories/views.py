from django.shortcuts import render
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
