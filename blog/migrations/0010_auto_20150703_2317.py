# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150703_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='url',
            field=models.URLField(verbose_name=b'Homepage', blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='gravatar_hash',
            field=models.CharField(default=0, max_length=32, editable=False),
        ),
    ]
