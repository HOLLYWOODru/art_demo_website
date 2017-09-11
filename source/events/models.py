from django.db import models

# класс событие
class Event(models.Model):

    # название события
    name = models.CharField(max_length=100, blank=True)

    # URL изображения события
    image_url = models.URLField()

    # короткая информация
    short_information = models.TextField(blank=True)

    # время начала события
    start_time = models.DateTimeField()

    # время конца события
    end_time = models.DateTimeField()

    # место проведения
    place = models.CharField(max_length=100, blank=True)

    # HTML code
    html = models.TextField(blank=True)

    def __str__(self):
        return self.name