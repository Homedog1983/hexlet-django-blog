from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path(
        '<str:tags>/<int:article_id>/',
        views.TagsIdView.as_view(),
        name='article_tags_id'
    ),
]
