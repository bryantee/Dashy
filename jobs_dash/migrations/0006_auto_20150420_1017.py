# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0005_job_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='status',
            new_name='is_open',
        ),
    ]
