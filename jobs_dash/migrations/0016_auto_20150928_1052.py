# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0015_auto_20150925_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='agent_email',
            field=models.EmailField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
