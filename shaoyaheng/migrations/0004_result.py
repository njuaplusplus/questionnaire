# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shaoyaheng', '0003_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.TextField(help_text=' ', verbose_name='\u6d4b\u8bd5\u7ed3\u679c')),
                ('user', models.OneToOneField(verbose_name='\u88ab\u6d4b\u8bd5\u8005', to='shaoyaheng.UserProfile')),
            ],
        ),
    ]
