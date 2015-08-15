# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shaoyaheng', '0005_info_next_page'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Info',
            new_name='Page',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='page',
            new_name='number',
        ),
    ]
