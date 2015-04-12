# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-created'], 'verbose_name': 'Blog Entry', 'verbose_name_plural': 'Blog Entries'},
        ),
        migrations.RemoveField(
            model_name='posts',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='posts',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 11, 3, 34, 13, 546000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 11, 3, 34, 25, 260000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
