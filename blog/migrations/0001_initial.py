# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('slug', models.SlugField(unique=True, max_length=60)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to=b'pictures/%Y/%m/%d')),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
