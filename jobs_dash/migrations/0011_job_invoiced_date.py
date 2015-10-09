# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0010_auto_20150714_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='invoiced_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 21, 22, 15, 22, 683483, tzinfo=utc), null=True, blank=True),
            preserve_default=False,
        ),
    ]
