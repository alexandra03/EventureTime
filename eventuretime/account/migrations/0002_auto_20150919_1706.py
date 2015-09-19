# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='access_token',
            field=models.TextField(null=True, help_text='Facebook token for offline access', blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='blog_url',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_name',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_open_graph',
            field=models.NullBooleanField(help_text='Determines if this user want to share via open graph'),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_profile_url',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(null=True, choices=[('m', 'Male'), ('f', 'Female')], blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to='images/facebook_profiles/%Y/%m/%d', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='new_token_required',
            field=models.BooleanField(help_text='Set to true if the access token is outdated or lacks permissions', default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='raw_data',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_id',
            field=models.BigIntegerField(null=True, blank=True, unique=True),
        ),
    ]
