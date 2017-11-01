# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171101_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date_modified',
            field=models.DateTimeField(),
        ),
    ]
