from django.urls import path

from hexlet_django_blog.categories import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='categories_index'),
]