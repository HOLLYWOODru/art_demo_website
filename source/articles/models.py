from django.db import models
from core.models import Artist

# класс статья
class Article(models.Model):

    # название
    name = models.CharField(max_length=100, blank=True)

    # URL изображения
    image_url = models.URLField()

    # HTML code
    html = models.TextField(blank=True)

    # информация
    short_information = models.TextField(blank=True)

    # дата создания
    creation_date = models.DateTimeField()

    # связь с художником (если есть)
    artist = models.OneToOneField(Artist, null=True, blank=True, related_name='article')

    def __str__(self):
        return self.name