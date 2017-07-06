# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170705_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttsxinfo',
            name='code',
            field=models.CharField(default=b'', max_length=6),
        ),
    ]
