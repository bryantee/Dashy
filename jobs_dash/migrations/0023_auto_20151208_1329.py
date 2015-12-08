# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0022_auto_20151204_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='invoice_number',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='address',
            field=models.CharField(unique=True, max_length=128, verbose_name=b'Address (No City)'),
        ),
    ]
