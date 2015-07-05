# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20150704_1349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['rank'], 'verbose_name': 'Seite', 'verbose_name_plural': 'Seiten'},
        ),
        migrations.AddField(
            model_name='page',
            name='rank',
            field=models.SmallIntegerField(default=0, verbose_name=b'Rang'),
        ),
    ]
