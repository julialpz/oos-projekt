# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20150704_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='rank',
            field=models.SmallIntegerField(unique=True, verbose_name=b'Rang'),
        ),
    ]
