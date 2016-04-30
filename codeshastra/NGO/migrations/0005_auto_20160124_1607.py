# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NGO', '0004_auto_20160124_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('mobile', models.IntegerField()),
                ('date', models.DateField(null=True, blank=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='volunteerprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='VolunteerProfile',
        ),
    ]
