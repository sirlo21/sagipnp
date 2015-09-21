# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metrado1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=25)),
                ('descripcion', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Metrado2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=25)),
                ('descripcion', models.TextField()),
                ('metrado1_id', models.ForeignKey(related_name='metrado_2', to='metrados.Metrado1')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Metrado3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=25)),
                ('descripcion', models.TextField()),
                ('metrado2_id', models.ForeignKey(related_name='metrado_3', to='metrados.Metrado2')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Metrado4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=25)),
                ('descripcion', models.TextField()),
                ('metrado3_id', models.ForeignKey(related_name='metrado_4', to='metrados.Metrado3')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
