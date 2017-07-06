# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ttsxinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=11)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
