from django.db import models
from core.models import Artist

class UserProfile(models.Model):
    user = models.OneToOneField(Artist)
    activation_key = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'User profiles'
