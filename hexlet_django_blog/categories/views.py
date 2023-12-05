from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from hexlet_django_blog.categories.models import Category
from .forms import CategoryForm


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


class CategoryFormCreateView(View):
    __template = 'categories/create.html'

    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        return render(request, self.__template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_index')
        return render(request, self.__template, {'form': form})


class CategoryFormEditView(View):

    def get(self, request, *args, **kwargs):
        category_id = kwargs.get('id')
        category = Category.objects.get(id=category_id)
        form = CategoryForm(instance=category)
        return render(
            request,
            'categories/update.html',
            {'form': form, 'category_id': category_id}
        )

    def post(self, request, *args, **kwargs):
        category_id = kwargs.get('id')
        category = Category.objects.get(id=category_id)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories_index')
        return render(
            request,
            'categories/update.html',
            {'form': form, 'category_id': category_id}
        )


class CategoryFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        category_id = kwargs.get('id')
        category = Category.objects.get(id=category_id)
        if category:
            category.delete()
        return redirect('categories_index')
