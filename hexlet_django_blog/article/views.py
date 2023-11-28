from django.shortcuts import render
from django.views import View


class IndexView(View):

    tags = ['Учебный проект', 'фреймворк Django (Python)', 'Статьи']
    template = 'articles/index.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template,
            context={'tags': self.tags},
        )
