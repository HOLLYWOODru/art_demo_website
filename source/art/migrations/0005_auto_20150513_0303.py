# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0004_auto_20150513_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='creator',
            field=models.ForeignKey(to='core.Artist', related_name='tags', blank=True),
        ),
    ]
