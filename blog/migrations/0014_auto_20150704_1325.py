# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150704_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='body',
            field=models.TextField(verbose_name=b'Inhalt', blank=True),
        ),
    ]
