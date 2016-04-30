# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0003_auto_20160124_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('registeredBy', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='sponsoredBy',
            field=models.CharField(max_length=150, blank=True, null=True),
        ),
    ]
