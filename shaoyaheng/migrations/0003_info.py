# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shaoyaheng', '0002_auto_20150815_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page', models.IntegerField(help_text=' ', verbose_name='\u9875\u7801')),
                ('info', models.TextField(help_text=' ', verbose_name='\u6d88\u606f')),
            ],
        ),
    ]
