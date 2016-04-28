# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ammapp', '0002_auto_20160428_0739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='Курс',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='Направление',
            new_name='direction',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='Уровень образования',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='Номер группы',
            new_name='number',
        ),
    ]
