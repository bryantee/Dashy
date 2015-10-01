# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0017_job_purchase_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='repair_po',
            field=models.FileField(upload_to=b'pos/', null=True, verbose_name=b'PO', blank=True),
            preserve_default=True,
        ),
    ]
