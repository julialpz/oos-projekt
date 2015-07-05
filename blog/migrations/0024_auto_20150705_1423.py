# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20150705_1422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['rank'], 'verbose_name': 'Seite', 'verbose_name_plural': 'Seiten'},
        ),
    ]
