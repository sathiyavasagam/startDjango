# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('OrderID', models.IntegerField()),
                ('CustomerID', models.CharField(unique=True, max_length=255)),
                ('EmployeeID', models.IntegerField()),
                ('OrderDate', models.DateTimeField()),
                ('RequiredDate', models.DateTimeField()),
                ('ShippedDate', models.DateTimeField()),
                ('ShipVia', models.IntegerField()),
                ('Freight', models.FloatField()),
            ],
        ),
    ]
