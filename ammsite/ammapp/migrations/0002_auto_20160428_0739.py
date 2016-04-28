# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ammapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='course',
            new_name='Курс',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='number',
            new_name='Номер группы',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='level',
            new_name='Уровень образования',
        ),
        migrations.AddField(
            model_name='group',
            name='Направление',
            field=models.TextField(blank=True),
        ),
    ]
