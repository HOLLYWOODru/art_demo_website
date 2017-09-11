from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Article

class ArticleListView(ListView):

    model = Article
    context_object_name = "articles"
    template_name = "articles/articles.html"
    paginate_by = settings.ARTICLES_COUNT_ON_PAGE

    def get_queryset(self):
        articles = Article.objects.order_by('-creation_date')

        return articles

class ArticleDetailView(DetailView):

    model = Article
    context_object_name = "article"
    template_name = "articles/article_detail.html"
