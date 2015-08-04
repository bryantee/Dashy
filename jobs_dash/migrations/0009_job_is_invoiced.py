# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0008_auto_20150518_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_invoiced',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
