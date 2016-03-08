# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elasticsearch1', '0004_auto_20160308_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='esquery',
            name='allq',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
