# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150919_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='access_token',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_id',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
