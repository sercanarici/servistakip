# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bayi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('bayi_adi', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Bayiler',
                'ordering': ('bayi_adi',),
                'verbose_name': 'Bayi',
            },
        ),
    ]
