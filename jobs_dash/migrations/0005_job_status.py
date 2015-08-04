# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0004_issue_is_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
