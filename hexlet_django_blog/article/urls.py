from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path(
        '',
        views.IndexView.as_view(),
        name='articles_index'),
    path(
        'create/',
        views.ArticleFormCreateView.as_view(),
        name='article_create'
    ),
    path(
        '<int:id>/',
        views.ArticleView.as_view(),
        name='article_id'),
]
