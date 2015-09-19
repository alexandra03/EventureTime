# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Yelp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=60)),
                ('token_secret', models.CharField(max_length=60)),
                ('consumer_key', models.CharField(max_length=60)),
                ('consumer_secret', models.CharField(max_length=60)),
            ],
        ),
    ]
