# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Seite', 'verbose_name_plural': 'Seiten'},
        ),
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=b'0', unique=True, verbose_name=b'Permalink'),
        ),
    ]
