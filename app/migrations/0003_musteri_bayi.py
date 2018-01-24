# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_bayi'),
    ]

    operations = [
        migrations.AddField(
            model_name='musteri',
            name='bayi',
            field=models.ForeignKey(related_name='musteriler', default=1, to='app.Bayi'),
            preserve_default=False,
        ),
    ]
