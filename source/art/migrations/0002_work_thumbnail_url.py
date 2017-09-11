# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='thumbnail_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
