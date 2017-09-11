# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('text', models.TextField()),
                ('added_date', models.DateTimeField()),
                ('avatar_url', models.URLField(blank=True, null=True)),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_surname', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('profile_url', models.URLField(blank=True, null=True)),
                ('sender', models.ForeignKey(to='core.Artist', blank=True, related_name='comments')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('information', models.TextField(blank=True)),
                ('creation_date', models.DateTimeField()),
                ('artist', models.ForeignKey(to='core.Artist', related_name='galleries')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('avatar_url', models.URLField(blank=True, null=True)),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_surname', models.CharField(blank=True, max_length=100)),
                ('profile_url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('theme', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('avatar_url', models.URLField(blank=True, null=True)),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_surname', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('profile_url', models.URLField(blank=True, null=True)),
                ('recipient', models.ForeignKey(to='core.Artist', related_name='recieved_messages')),
                ('sender', models.ForeignKey(to='core.Artist', blank=True, related_name='sent_messages')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('information', models.TextField()),
                ('type', models.IntegerField(choices=[(0, 'System notification'), (1, 'Work has been rejected'), (2, 'Tag has been rejected')], default=0)),
                ('recipient', models.ForeignKey(to='core.Artist', related_name='notifications')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('creator', models.ForeignKey(to='core.Artist', blank=True, related_name='tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('image_url', models.URLField()),
                ('information', models.TextField(blank=True)),
                ('status', models.IntegerField(choices=[(0, 'waiting for review'), (1, 'approved'), (2, 'rejected')], default=0)),
                ('creation_date', models.DateTimeField()),
                ('form_of_art', models.IntegerField(choices=[(0, 'не выбран'), (1, 'живопись'), (2, 'графика'), (3, 'скульптура'), (4, 'фотоискусство'), (5, 'граффити'), (6, 'комикс'), (7, 'татуировка')], default=0)),
                ('genre_of_art', models.IntegerField(choices=[(0, 'не выбран'), (1, 'исторический'), (2, 'мифологический'), (3, 'батальный'), (4, 'портрет'), (5, 'пейзаж'), (6, 'натюрморт'), (7, 'бытовой'), (8, 'марина'), (9, 'анималистический'), (10, 'интерьер')], default=0)),
                ('technique_of_art', models.IntegerField(choices=[(0, 'не выбрана'), (1, 'акварель'), (2, 'алла прима'), (3, 'аэрография'), (4, 'батик'), (5, 'витраж'), (6, 'горячая эмаль'), (7, 'гравюра'), (8, 'граттаж'), (9, 'гризайль'), (10, 'гуашь'), (11, 'декоративная живопись'), (12, 'коллаж'), (13, 'литография'), (14, 'маркетри'), (15, 'мозаика'), (16, 'монументальная живопись'), (17, 'пастель'), (18, 'станковая живопись'), (19, 'сухая кисть'), (20, 'тушь'), (21, 'шелкография'), (22, 'эстамп')], default=0)),
                ('style_of_art', models.IntegerField(choices=[(0, 'не выбрано'), (1, 'абстракционизм'), (2, 'импрессионизм'), (3, 'экспрессионизм'), (4, 'aвангардизм'), (5, 'aкадемизм'), (6, 'aкционизм'), (7, 'aмпир'), (8, 'aналитический кубизм'), (9, 'aналитическое искусство'), (10, 'aнахронизм'), (11, 'aр нуво'), (12, 'aр брют'), (13, 'aрте повера'), (14, 'aрт деко')], default=0)),
                ('artist', models.ForeignKey(to='core.Artist', blank=True, null=True, related_name='works')),
                ('artist_likes', models.ManyToManyField(blank=True, null=True, related_name='liked_works', to='core.Artist')),
                ('colors', models.ManyToManyField(blank=True, null=True, to='art.Color')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='art.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='notification',
            name='tag',
            field=models.OneToOneField(to='art.Tag', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notification',
            name='work',
            field=models.OneToOneField(to='art.Work', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='work',
            field=models.ForeignKey(to='art.Work', related_name='likes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='works',
            field=models.ManyToManyField(blank=True, null=True, related_name='galleries', to='art.Work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='work',
            field=models.ForeignKey(to='art.Work', related_name='comments'),
            preserve_default=True,
        ),
    ]
