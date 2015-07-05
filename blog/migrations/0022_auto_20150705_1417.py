# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20150704_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='rank',
            field=models.SmallIntegerField(help_text=b'Bestimmt Reihenfolge im Hauptmen\xc3\xbc, bei leerem Feld erscheint Seite nicht im Men\xc3\xbc.', unique=True, verbose_name=b'Rang', blank=True),
        ),
    ]
