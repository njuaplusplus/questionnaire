# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shaoyaheng', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(help_text=' ', verbose_name='\u5e74\u9f84'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='number',
            field=models.IntegerField(help_text=' ', verbose_name='\u7f16\u53f7'),
        ),
    ]
