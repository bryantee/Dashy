# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_dash', '0002_auto_20150410_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=128)),
                ('job', models.ForeignKey(to='jobs_dash.Job')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
