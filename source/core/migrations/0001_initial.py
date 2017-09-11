# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtifexUser',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, auto_created=True, to=settings.AUTH_USER_MODEL, parent_link=True, primary_key=True)),
                ('user_type', models.IntegerField(choices=[(0, 'Artist'), (1, 'Artist moderator'), (2, 'News moderator')], default=0)),
                ('user_sex', models.IntegerField(choices=[(0, 'не указан'), (1, 'мужской'), (2, 'женский')], default=0)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artifexuser_ptr', models.OneToOneField(serialize=False, auto_created=True, to='core.ArtifexUser', parent_link=True, primary_key=True)),
                ('avatar_url', models.URLField(null=True, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('site_url', models.URLField(null=True, blank=True)),
                ('twitter_name', models.CharField(max_length=100, blank=True)),
                ('information', models.TextField(blank=True)),
                ('has_artifex_article', models.BooleanField(default=False)),
                ('artifex_article_url', models.URLField(null=True, blank=True)),
                ('is_activated', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Artists',
            },
            bases=('core.artifexuser',),
        ),
    ]
