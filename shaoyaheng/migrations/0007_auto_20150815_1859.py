# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shaoyaheng', '0006_auto_20150815_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='info',
            new_name='page',
        ),
    ]
