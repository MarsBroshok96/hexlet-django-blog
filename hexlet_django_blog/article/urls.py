from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<slug:tags>/<int:article_id>/',
         views.gen_article_from_url, name='article'
         ),
]
