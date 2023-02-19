from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from hexlet_django_blog.article.models import Article


def gen_article_from_url(request, tags, article_id):
    return render(request, 'articles/article_from_url.html', context={
        'article_id': article_id,
        'tags': tags,
    })


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })
