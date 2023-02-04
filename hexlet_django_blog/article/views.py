from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


def index(request, tags, article_id):
    return render(request, 'article/index.html', context={
        'article_id': article_id,
        'tags': tags,
    })


#class IndexView(View):

#    def get(self, request, *args, **kwargs):
#        return HttpResponse('Articles')
# def indexs(request):
#    return render(request, 'article/index.html', context={
#        'article': 'first article'
#    })
