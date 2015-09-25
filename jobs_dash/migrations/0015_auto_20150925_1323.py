# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0014_auto_20150924_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='agent_email',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='agent_name',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='agent_phone',
            field=models.CharField(max_length=12, blank=True),
            preserve_default=True,
        ),
    ]
