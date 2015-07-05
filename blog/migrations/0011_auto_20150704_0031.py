# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150703_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='gravatar_hash',
            field=models.CharField(max_length=32, editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
