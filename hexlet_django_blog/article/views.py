from django.shortcuts import render


def index(request):
    tags = ['Учебный проект', 'фреймворк Django (Python)', 'Статьи']
    return render(
        request,
        'articles/index.html',
        context={'tags': tags},
    )
