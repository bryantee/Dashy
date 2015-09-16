# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0011_job_invoiced_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_paid',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='is_paid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='invoiced_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
