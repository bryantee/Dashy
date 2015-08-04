# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0009_job_is_invoiced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_invoiced',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
