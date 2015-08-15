# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shaoyaheng', '0004_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='next_page',
            field=models.CharField(default=0, help_text=' ', max_length=255, verbose_name='\u4e0b\u4e00\u9875'),
            preserve_default=False,
        ),
    ]
