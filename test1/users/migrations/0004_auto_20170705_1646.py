# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170705_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ttsxinfo',
            name='pwd',
            field=models.CharField(max_length=50),
        ),
    ]
