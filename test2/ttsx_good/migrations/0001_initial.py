# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goodsinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('pic', models.ImageField(upload_to=b'goods/')),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gclick', models.IntegerField()),
                ('unit', models.CharField(max_length=10)),
                ('isdelete', models.BooleanField(default=False)),
                ('tilte', models.CharField(max_length=200)),
                ('kucun', models.IntegerField(default=100)),
                ('describe', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Typeinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typename', models.CharField(max_length=20)),
                ('isdelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='typegood',
            field=models.ForeignKey(to='ttsx_good.Typeinfo'),
        ),
    ]
