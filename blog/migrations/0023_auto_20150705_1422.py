# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20150705_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Seite', 'verbose_name_plural': 'Seiten'},
        ),
        migrations.AlterField(
            model_name='page',
            name='rank',
            field=models.SmallIntegerField(help_text=b'Bestimmt Reihenfolge im Hauptmen\xc3\xbc, bei leerem Feld erscheint Seite nicht im Men\xc3\xbc.', unique=True, null=True, verbose_name=b'Rang', blank=True),
        ),
    ]
