# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musteri',
            name='bayi',
            field=models.ForeignKey(related_name='musteriler', to='app.Bayi', default=1),
        ),
    ]
