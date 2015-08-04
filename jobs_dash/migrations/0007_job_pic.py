# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0006_auto_20150420_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pic',
            field=models.ImageField(upload_to=b'images/', null=True, verbose_name=b'House Pic', blank=True),
            preserve_default=True,
        ),
    ]
