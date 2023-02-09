from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

# Register your models here.
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['name', 'body']
    list_display = ('name', 'timestamp')
    list_filter = (('timestamp', DateFieldListFilter),)