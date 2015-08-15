# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shaoyaheng', '0007_auto_20150815_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='page',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='number',
            new_name='page_num',
        ),
    ]
