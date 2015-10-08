# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levantamiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document', models.FileField(upload_to=b'docs/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('document_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='metrados.Document')),
            ],
            options={
            },
            bases=('metrados.document',),
        ),
        migrations.CreateModel(
            name='FichaTecnica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField(default=0)),
                ('largo', models.FloatField(default=0)),
                ('ancho', models.FloatField(default=0)),
                ('alto', models.FloatField(default=0)),
                ('parcial', models.IntegerField(default=0)),
                ('unidad', models.IntegerField(default=0)),
                ('punitario', models.IntegerField(default=0)),
                ('form', models.ForeignKey(related_name='ficha_tecnica', to='levantamiento.Levantamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('image_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='metrados.Image')),
                ('form', models.ForeignKey(related_name='images', to='metrados.FichaTecnica')),
            ],
            options={
            },
            bases=('metrados.image',),
        ),
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
                ('metrado1', models.ForeignKey(related_name='metrado_2', to='metrados.Metrado1')),
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
                ('metrado2', models.ForeignKey(related_name='metrado_3', to='metrados.Metrado2')),
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
                ('metrado3', models.ForeignKey(related_name='metrado_4', to='metrados.Metrado3')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='metrado1',
            field=models.ForeignKey(related_name='ficha_tecnica', to='metrados.Metrado1'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='metrado2',
            field=models.ForeignKey(related_name='ficha_tecnica', to='metrados.Metrado2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='metrado3',
            field=models.ForeignKey(related_name='ficha_tecnica', to='metrados.Metrado3'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='metrado4',
            field=models.ForeignKey(related_name='ficha_tecnica', to='metrados.Metrado4'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doc',
            name='form',
            field=models.ForeignKey(related_name='documents', blank=True, to='metrados.FichaTecnica', null=True),
            preserve_default=True,
        ),
    ]
