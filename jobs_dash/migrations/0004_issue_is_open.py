# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0003_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='is_open',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
