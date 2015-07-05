# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150701_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=60, verbose_name=b'Name')),
                ('email', models.EmailField(max_length=254, verbose_name=b'E-Mail')),
                ('body', models.TextField(verbose_name=b'Inhalt')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Erstellt am')),
                ('published', models.BooleanField(default=True, verbose_name=b'Ver\xc3\xb6ffentlicht?')),
                ('post', models.ForeignKey(to='blog.Post')),
            ],
            options={
                'verbose_name': 'Kommentar',
                'verbose_name_plural': 'Kommentare',
            },
        ),
    ]
