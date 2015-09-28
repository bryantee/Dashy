# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0016_auto_20150928_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='purchase_order',
            field=models.FileField(upload_to=b'pos/', null=True, verbose_name=b'Purchase Order', blank=True),
            preserve_default=True,
        ),
    ]
