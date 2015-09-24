# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0013_auto_20150916_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='flooring',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='flooring_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
