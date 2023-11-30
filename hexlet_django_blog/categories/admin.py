from django.contrib import admin
from .models import Category


@admin.register(Category)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name', 'description']
