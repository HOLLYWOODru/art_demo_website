from django.conf.urls import patterns, url
from .views import ArticleDetailView, ArticleListView

articles_urlpatterns = patterns('',
    url(r'^$', ArticleListView.as_view(), name='home'),
    url(r'^articles/$', ArticleListView.as_view(), name='articles'),
    url(r'^articles?([\w-]+)/$', ArticleListView.as_view(), name='articles'),
    url(r'^articles/репортаж$', ArticleListView.as_view(), name='articles.report'),
    url(r'^articles/живопись$', ArticleListView.as_view(), name='articles.art'),
    url(r'^articles/фотография$', ArticleListView.as_view(), name='articles.photo'),
    url(r'^articles/татуировка$', ArticleListView.as_view(), name='articles.tattoo'),
    url(r'^articles/скульптура$', ArticleListView.as_view(), name='articles.sculpture'),
    url(r'^articles/стрит-арт$', ArticleListView.as_view(), name='articles.street-art'),
    url(r'^articles/музыка$', ArticleListView.as_view(), name='articles.music'),
    url(r'^articles/кино$', ArticleListView.as_view(), name='articles.films'),
    url(r'^articles/цифра$', ArticleListView.as_view(), name='articles.digit'),
    url(r'^articles/(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name='articles.detail'),
)
