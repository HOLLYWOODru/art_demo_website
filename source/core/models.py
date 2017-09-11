from django.db import models
from django.contrib.auth.models import User

# псевдоабстрактный класс Пользователь портала
class ArtifexUser(User):

    # все возможные типы пользователя
    USER_TYPE_ARTIST = 0
    USER_TYPE_ARTIST_MODERATOR = 1
    USER_TYPE_NEWS_MODERATOR = 2

    ARTIFEX_USER_TYPES = (
        (USER_TYPE_ARTIST, 'Artist'),
        (USER_TYPE_ARTIST_MODERATOR, 'Artist moderator'),
        (USER_TYPE_NEWS_MODERATOR, 'News moderator'),
    )

    # все возможные полы пользователя
    USER_SEX_NO = 0
    USER_SEX_MALE = 1
    USER_SEX_FEMALE = 2

    USER_SEX_TYPES = (
        (USER_SEX_NO, 'не указан'),
        (USER_SEX_MALE, 'мужской'),
        (USER_SEX_FEMALE, 'женский'),
    )

    # тип пользователя
    user_type = models.IntegerField(choices=ARTIFEX_USER_TYPES, default=USER_TYPE_ARTIST)

    # пол пользователя
    user_sex = models.IntegerField(choices=USER_SEX_TYPES, default=USER_SEX_NO)


# - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *
# класс художник
class Artist(ArtifexUser):

    # URL аватара
    avatar_url = models.URLField(null=True, blank=True)

    # дата рождения
    birth_date = models.DateField(null=True, blank=True)

    # URL сайта
    site_url = models.URLField(null=True, blank=True)

    # ник в Twitter
    twitter_name = models.CharField(max_length=100, blank=True)

    # информация
    information = models.TextField(blank=True)

    # есть ли статья на artifex.ru
    has_artifex_article = models.BooleanField(default=False)

    # URL статьи на artifex.ru
    artifex_article_url = models.URLField(null=True, blank=True)

    # активирован ли пользователь
    is_activated = models.BooleanField(default=True)

    class Meta:

        verbose_name_plural = 'Artists'