# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 20, 4, 6, 9464, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 20, 4, 20, 895549, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
