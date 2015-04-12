# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_posts_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
