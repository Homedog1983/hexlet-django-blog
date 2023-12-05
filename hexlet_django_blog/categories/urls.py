from django.urls import path

from hexlet_django_blog.categories import views

urlpatterns = [
    path(
        '',
        views.IndexView.as_view(),
        name='categories_index'
    ),
    path(
        'create/',
        views.CategoryFormCreateView.as_view(),
        name='category_create'
    ),
    path(
        '<int:id>/edit/',
        views.CategoryFormEditView.as_view(),
        name='category_update'),
    path(
        '<int:id>/delete/',
        views.CategoryFormDeleteView.as_view(),
        name='category_delete'),
    path(
        '<int:id>/',
        views.CategoryView.as_view(),
        name='category_id'
    ),
]
