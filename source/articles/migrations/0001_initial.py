# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('image_url', models.URLField()),
                ('html', models.TextField(blank=True)),
                ('short_information', models.TextField(blank=True)),
                ('creation_date', models.DateTimeField()),
                ('artist', models.OneToOneField(null=True, related_name='article', blank=True, to='core.Artist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
