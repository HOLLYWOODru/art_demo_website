from django.db import models
from core.models import Artist
from django.contrib.auth.models import User

# - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *
# класс Цвет
class Color(models.Model):

    # название
    name = models.CharField(max_length=20)


# - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *
# класс Тэг
class Tag(models.Model):

    # название
    name = models.CharField(max_length=50)

    # создатель
    creator = models.ForeignKey(User, related_name='tags', blank=True)

    def __str__(self):
        return self.name


# - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *
# класс работа художника
class Work(models.Model):
    # все возможные виды искусства
    ART_FORMS = (
        (0, 'не выбран'),
        (1, 'живопись'),
        (2, 'графика'),
        (3, 'скульптура'),
        (4, 'фотоискусство'),
        (5, 'граффити'),
        (6, 'комикс'),
        (7, 'татуировка'),
    )

    # все возможные жанры искусства
    ART_GENRES = (
        (0, 'не выбран'),
        (1, 'исторический'),
        (2, 'мифологический'),
        (3, 'батальный'),
        (4, 'портрет'),
        (5, 'пейзаж'),
        (6, 'натюрморт'),
        (7, 'бытовой'),
        (8, 'марина'),
        (9, 'анималистический'),
        (10, 'интерьер'),
    )

    # все возможные техники исполнения
    ART_TECHNIQUES = (
        (0, 'не выбрана'),
        (1, 'акварель'),
        (2, 'алла прима'),
        (3, 'аэрография'),
        (4, 'батик'),
        (5, 'витраж'),
        (6, 'горячая эмаль'),
        (7, 'гравюра'),
        (8, 'граттаж'),
        (9, 'гризайль'),
        (10, 'гуашь'),
        (11, 'декоративная живопись'),
        (12, 'коллаж'),
        (13, 'литография'),
        (14, 'маркетри'),
        (15, 'мозаика'),
        (16, 'монументальная живопись'),
        (17, 'пастель'),
        (18, 'станковая живопись'),
        (19, 'сухая кисть'),
        (20, 'тушь'),
        (21, 'шелкография'),
        (22, 'эстамп'),
        (23, 'масло на холсте'),
    )

    # все возможные направления в искусстве
    ART_STYLES = (
        (0, 'не выбрано'),
        (1, 'абстракционизм'),
        (2, 'импрессионизм'),
        (3, 'экспрессионизм'),
        (4, 'aвангардизм'),
        (5, 'aкадемизм'),
        (6, 'aкционизм'),
        (7, 'aмпир'),
        (8, 'aналитический кубизм'),
        (9, 'aналитическое искусство'),
        (10, 'aнахронизм'),
        (11, 'aр нуво'),
        (12, 'aр брют'),
        (13, 'aрте повера'),
        (14, 'aрт деко'),
    )

    # статус проверки работы модератором
    ART_IS_WAITING_FOR_REVIEW = 0
    ART_WAS_APPROVED = 1
    ART_WAS_REJECTED = 2

    ART_REVIEW_STATUSES = (
        (ART_IS_WAITING_FOR_REVIEW, 'waiting for review'),
        (ART_WAS_APPROVED, 'approved'),
        (ART_WAS_REJECTED, 'rejected'),
    )

    # название
    name = models.CharField(max_length=100, blank=True)

    # URL изображения
    image_url = models.URLField()

    # URL thumbnail-а
    thumbnail_url = models.URLField()

    # информация
    information = models.TextField(blank=True)

    # статус работы
    status = models.IntegerField(choices=ART_REVIEW_STATUSES, default=ART_IS_WAITING_FOR_REVIEW)

    # дата создания
    creation_date = models.DateTimeField()

    # вид искусства
    form_of_art = models.IntegerField(choices=ART_FORMS, default=0)

    # жанр
    genre_of_art = models.IntegerField(choices=ART_GENRES, default=0)

    # техника
    technique_of_art = models.IntegerField(choices=ART_TECHNIQUES, default=0)

    # направление
    style_of_art = models.IntegerField(choices=ART_STYLES, default=0)

    # художник
    artist = models.ForeignKey(Artist, related_name='works', null=True, blank=True)

    # цвета
    colors = models.ManyToManyField(Color, null=True, blank=True)

    # тэги
    tags = models.ManyToManyField(Tag, null=True,  blank=True)

    # лайкнувшие художники
    artist_likes = models.ManyToManyField(Artist, related_name='liked_works', null=True, blank=True)

    def __str__(self):
        return self.name

# - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *
# класс Галерея
class Gallery(models.Model):

    # название Галереи
    name = models.CharField(max_length=100)

    # информация
    information = models.TextField(blank=True)

    # дата создания
    creation_date = models.DateTimeField()

    # работы в галерее
    works = models.ManyToManyField(Work, related_name='galleries', null=True, blank=True)

    # художник
    artist = models.ForeignKey(Artist, related_name='galleries')

# - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *
# класс Like (посетителя)
class Like(models.Model):

    # URL аватара лайкнувшего
    avatar_url = models.URLField(null=True, blank=True)

    # имя лайкнувшего
    sender_name = models.CharField(max_length=100)

    # фамилия лайкнувшего
    sender_surname = models.CharField(max_length=100, blank=True)

    # URL профиля социальной сети
    profile_url = models.URLField()

    # работа, которую лайнули
    work = models.ForeignKey(Work, related_name='likes')

# - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *
# класс Уведомление
class Notification(models.Model):

    # все возможные типы уведомлений
    NOTIFICATION_TYPE_SYSTEM = 0
    NOTIFICATION_TYPE_WORK_REJECTED = 1
    NOTIFICATION_TYPE_TAG_REJECTED = 2

    NOTIFICATION_TYPES = (
        (NOTIFICATION_TYPE_SYSTEM, 'System notification'),
        (NOTIFICATION_TYPE_WORK_REJECTED, 'Work has been rejected'),
        (NOTIFICATION_TYPE_TAG_REJECTED, 'Tag has been rejected'),
    )

    # название
    name = models.CharField(max_length=100)

    # текст уведомления
    information = models.TextField()

    # тип уведомления
    type = models.IntegerField(choices=NOTIFICATION_TYPES, default=NOTIFICATION_TYPE_SYSTEM)

    # получатель
    recipient = models.ForeignKey(Artist, related_name='notifications')

    # работа (если уведомление о работе)
    work = models.OneToOneField(Work, null=True, blank=True)

    # тэг (если уведомление о тэге)
    tag = models.OneToOneField(Tag, null=True, blank=True)

# - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *
# класс Сообщение
class Message(models.Model):

    # название
    theme = models.CharField(max_length=100)

    # текст сообщения
    text = models.TextField()

    # URL аватара
    avatar_url = models.URLField(null=True, blank=True)

    # имя отправителя
    sender_name = models.CharField(max_length=100)

    # фамилия отправителя
    sender_surname = models.CharField(max_length=100, blank=True)

    # email отправителя
    email = models.EmailField()

    # URL профиля социальной сети
    profile_url = models.URLField(null=True, blank=True)

    # получатель
    recipient = models.ForeignKey(Artist, related_name='recieved_messages')

    # отправитель (если это художник)
    sender = models.ForeignKey(Artist, related_name='sent_messages', blank=True)

# - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *
# класс Комментарий
class Comment(models.Model):

    # текст комментария
    text = models.TextField()

    # дата добавления
    added_date = models.DateTimeField()

    # URL аватара
    avatar_url = models.URLField(null=True, blank=True)

    # имя отправителя
    sender_name = models.CharField(max_length=100)

    # фамилия отправителя
    sender_surname = models.CharField(max_length=100, blank=True)

    # email обратной связи
    email = models.EmailField()

    # URL профиля социальной сети
    profile_url = models.URLField(null=True, blank=True)

    # работа, которую комментриуют
    work = models.ForeignKey(Work, related_name = 'comments')

    # отправитель (если это художник)
    sender = models.ForeignKey(Artist, related_name = 'comments', blank=True)