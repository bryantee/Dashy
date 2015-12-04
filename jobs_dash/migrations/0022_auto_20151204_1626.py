# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0021_auto_20151204_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='city',
            field=models.ForeignKey(verbose_name=b'City', blank=True, to='jobs_dash.City', null=True),
        ),
    ]
