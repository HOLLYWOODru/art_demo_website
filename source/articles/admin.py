from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):

    list_display = ('name',  'creation_date', 'artist')
    list_filter = ('name', 'creation_date')
    search_fields = ['name']

admin.site.register(Article, ArticleAdmin)