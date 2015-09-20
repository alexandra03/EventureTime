# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpart',
            name='category',
            field=models.CharField(default='place', choices=[('food', 'Food'), ('club', 'Club'), ('movie', 'Movie'), ('place', 'Place'), ('other', 'Other'), ('sports', 'Sports'), ('concert', 'Concert')], max_length=20),
        ),
    ]
