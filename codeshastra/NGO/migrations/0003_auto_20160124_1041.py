# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0002_student_average'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='sponsoredBy',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
