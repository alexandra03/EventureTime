# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uber',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('client_id', models.CharField(max_length=60)),
                ('client_secret', models.CharField(max_length=60)),
                ('secret', models.CharField(max_length=60)),
                ('server_token', models.CharField(max_length=60)),
            ],
        ),
    ]
