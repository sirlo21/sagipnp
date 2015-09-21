# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ayuda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('form', models.CharField(max_length=300)),
                ('posicion', models.IntegerField(null=True, blank=True)),
                ('title', models.CharField(max_length=40, blank=True)),
                ('text', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
