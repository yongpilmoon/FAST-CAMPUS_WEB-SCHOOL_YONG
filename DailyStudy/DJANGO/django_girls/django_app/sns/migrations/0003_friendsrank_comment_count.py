# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0002_friendsrank_friends_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendsrank',
            name='comment_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]