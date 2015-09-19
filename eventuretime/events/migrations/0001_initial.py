# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tag', models.CharField(max_length=20)),
                ('public', models.BooleanField(default=False)),
                ('facebook', models.CharField(max_length=100)),
                ('attending', models.ManyToManyField(related_name='events_attending', to='account.Profile')),
                ('invited', models.ManyToManyField(related_name='events_invited_to', to='account.Profile')),
                ('owner', models.ForeignKey(related_name='events_owned', to='account.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='EventPart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'place', max_length=20, choices=[(b'food', b'Food'), (b'club', b'Club'), (b'movie', b'Movie'), (b'place', b'Place'), (b'other', b'Other'), (b'sports', b'Sports'), (b'concert', b'Concert')])),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('country', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('venue', models.CharField(max_length=50)),
                ('estimated_cost', models.IntegerField()),
                ('event', models.ForeignKey(related_name='event', to='events.Event')),
            ],
        ),
    ]
