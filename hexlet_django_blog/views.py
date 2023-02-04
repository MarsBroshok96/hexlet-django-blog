from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse


def index(request):
    return redirect(reverse('article', kwargs={'tags':'python', 'article_id': 42}))


class HomeView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )