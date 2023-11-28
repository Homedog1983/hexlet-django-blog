from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


def about(request):
    topics = ['Hexlet training project', 'Python', 'Django']
    return render(
        request,
        'about.html',
        context={'topics': topics},
    )
