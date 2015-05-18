# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0007_job_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='price',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
    ]
