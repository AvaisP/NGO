# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=150)),
                ('district', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField(default=0)),
                ('location', models.IntegerField(default=400010)),
                ('days_present', models.IntegerField(default=0)),
                ('days_total', models.IntegerField(default=0)),
                ('marks', models.TextField(blank=True)),
                ('sponsored', models.BooleanField(default=False)),
                ('school', models.ForeignKey(to='NGO.School')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('contact', models.IntegerField(unique=True, default=0)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
