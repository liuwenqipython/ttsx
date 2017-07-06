# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170705_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ttsxinfo',
            name='address',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='ttsxinfo',
            name='phone',
            field=models.CharField(default=b'', max_length=11),
        ),
    ]
