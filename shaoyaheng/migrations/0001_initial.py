# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=0, help_text=' ', verbose_name='\u7f16\u53f7')),
                ('age', models.IntegerField(default=0, help_text=' ', verbose_name='\u5e74\u9f84')),
                ('gender', models.CharField(default=b'M', help_text=' ', max_length=2, verbose_name='\u6027\u522b', choices=[(b'M', '\u7537'), (b'F', '\u5973')])),
                ('grade', models.CharField(help_text=' ', max_length=255, verbose_name='\u5e74\u7ea7')),
                ('major', models.CharField(help_text=' ', max_length=255, verbose_name='\u4e13\u4e1a')),
            ],
        ),
    ]
