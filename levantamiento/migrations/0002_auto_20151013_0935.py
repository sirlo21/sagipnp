# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levantamiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='levantamiento',
            name='telefono_fijo_comisaria',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
