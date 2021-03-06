# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0005_auto_20150513_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='tags', blank=True),
        ),
    ]
