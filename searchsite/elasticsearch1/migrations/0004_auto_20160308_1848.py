# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elasticsearch1', '0003_auto_20160308_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='esquery',
            name='allq',
        ),
        migrations.RemoveField(
            model_name='esquery',
            name='author',
        ),
        migrations.RemoveField(
            model_name='esquery',
            name='date1',
        ),
        migrations.RemoveField(
            model_name='esquery',
            name='date2',
        ),
        migrations.RemoveField(
            model_name='esquery',
            name='occur',
        ),
        migrations.RemoveField(
            model_name='esquery',
            name='source',
        ),
    ]
