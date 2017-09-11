# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0003_auto_20150508_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='technique_of_art',
            field=models.IntegerField(choices=[(0, 'не выбрана'), (1, 'акварель'), (2, 'алла прима'), (3, 'аэрография'), (4, 'батик'), (5, 'витраж'), (6, 'горячая эмаль'), (7, 'гравюра'), (8, 'граттаж'), (9, 'гризайль'), (10, 'гуашь'), (11, 'декоративная живопись'), (12, 'коллаж'), (13, 'литография'), (14, 'маркетри'), (15, 'мозаика'), (16, 'монументальная живопись'), (17, 'пастель'), (18, 'станковая живопись'), (19, 'сухая кисть'), (20, 'тушь'), (21, 'шелкография'), (22, 'эстамп'), (23, 'масло на холсте')], default=0),
        ),
    ]
