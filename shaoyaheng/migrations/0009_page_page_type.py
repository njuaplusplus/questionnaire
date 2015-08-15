# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shaoyaheng', '0008_auto_20150815_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_type',
            field=models.CharField(default=b'I', help_text=' ', max_length=2, verbose_name='\u9875\u9762\u7c7b\u578b', choices=[(b'I', '\u8bf4\u660e'), (b'Q', '\u6d4b\u8bd5')]),
        ),
    ]
