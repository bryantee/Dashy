# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0012_auto_20150914_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='date_paid',
            new_name='paid_date',
        ),
    ]
