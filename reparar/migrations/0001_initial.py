# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levantamiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoDeEjecucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstalacionElectrica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inst_elect_descripcion', models.TextField()),
                ('inst_elect_numero_unidad_medida', models.PositiveIntegerField(default=0, max_length=20)),
                ('inst_elect_dimensiones', models.CharField(max_length=150)),
                ('inst_elect_precio_unitario', models.PositiveIntegerField(default=0)),
                ('inst_elect_precio_total_referencial', models.PositiveIntegerField(default=0)),
                ('inst_elect_tiempo_ejecucion', models.PositiveIntegerField()),
                ('inst_elect_img', models.ImageField(upload_to=b'images/')),
                ('inst_elect_doc', models.FileField(upload_to=b'docs/')),
                ('inst_elect_observaciones', models.TextField(null=True, blank=True)),
                ('inst_elect_vigente', models.BooleanField(default=True)),
                ('inst_elect_pub_data', models.DateTimeField(auto_now=True)),
                ('inst_elect_estado_ejecucion', models.ForeignKey(to='reparar.EstadoDeEjecucion')),
                ('inst_elect_form', models.ForeignKey(related_name='instalaciones_electricas', to='levantamiento.Levantamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstalacionSanitaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inst_sant_descripcion', models.TextField()),
                ('inst_sant_numero_unidad_medida', models.PositiveIntegerField(default=0, max_length=20)),
                ('inst_sant_dimensiones', models.CharField(max_length=150)),
                ('inst_sant_precio_unitario', models.PositiveIntegerField(default=0)),
                ('inst_sant_precio_total_referencial', models.PositiveIntegerField(default=0)),
                ('inst_sant_tiempo_ejecucion', models.PositiveIntegerField()),
                ('inst_sant_img', models.ImageField(upload_to=b'images/')),
                ('inst_sant_doc', models.FileField(upload_to=b'docs/')),
                ('inst_sant_observaciones', models.TextField(null=True, blank=True)),
                ('inst_sant_vigente', models.BooleanField(default=True)),
                ('inst_sant_pub_data', models.DateTimeField(auto_now=True)),
                ('inst_sant_estado_ejecucion', models.ForeignKey(to='reparar.EstadoDeEjecucion')),
                ('inst_sant_form', models.ForeignKey(related_name='instalaciones_sanitarias', to='levantamiento.Levantamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MurosParedes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mp_descripcion', models.TextField()),
                ('mp_numero_unidad_medida', models.PositiveIntegerField(default=0, max_length=20)),
                ('mp_dimensiones', models.CharField(max_length=150)),
                ('mp_precio_unitario', models.PositiveIntegerField(default=0)),
                ('mp_precio_total_referencial', models.PositiveIntegerField(default=0)),
                ('mp_tiempo_ejecucion', models.PositiveIntegerField()),
                ('mp_img', models.ImageField(upload_to=b'images/')),
                ('mp_doc', models.FileField(upload_to=b'docs/')),
                ('mp_observaciones', models.TextField(null=True, blank=True)),
                ('mp_vigente', models.BooleanField(default=True)),
                ('mp_pub_data', models.DateTimeField(auto_now=True)),
                ('mp_estado_ejecucion', models.ForeignKey(to='reparar.EstadoDeEjecucion')),
                ('mp_form', models.ForeignKey(related_name='muros_paredes', to='levantamiento.Levantamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Techo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('techo_descripcion', models.TextField()),
                ('techo_numero_unidad_medida', models.PositiveIntegerField(default=0, max_length=20)),
                ('techo_dimensiones', models.CharField(max_length=150)),
                ('techo_precio_unitario', models.PositiveIntegerField(default=0)),
                ('techo_precio_total_referencial', models.PositiveIntegerField(default=0)),
                ('techo_tiempo_ejecucion', models.PositiveIntegerField()),
                ('techo_img', models.ImageField(upload_to=b'images/')),
                ('techo_doc', models.FileField(upload_to=b'docs/')),
                ('techo_observaciones', models.TextField(null=True, blank=True)),
                ('techo_vigente', models.BooleanField(default=True)),
                ('techo_pub_data', models.DateTimeField(auto_now=True)),
                ('techo_estado_ejecucion', models.ForeignKey(to='reparar.EstadoDeEjecucion')),
                ('techo_form', models.ForeignKey(related_name='techos', to='levantamiento.Levantamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoDeReparacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reparacion', models.CharField(max_length=900)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MPReparacion',
            fields=[
                ('tipodereparacion_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='reparar.TipoDeReparacion')),
            ],
            options={
            },
            bases=('reparar.tipodereparacion',),
        ),
        migrations.CreateModel(
            name='ISReparacion',
            fields=[
                ('tipodereparacion_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='reparar.TipoDeReparacion')),
            ],
            options={
            },
            bases=('reparar.tipodereparacion',),
        ),
        migrations.CreateModel(
            name='IEReparacion',
            fields=[
                ('tipodereparacion_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='reparar.TipoDeReparacion')),
            ],
            options={
            },
            bases=('reparar.tipodereparacion',),
        ),
        migrations.CreateModel(
            name='TipoDeTecho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TReparacion',
            fields=[
                ('tipodereparacion_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='reparar.TipoDeReparacion')),
            ],
            options={
            },
            bases=('reparar.tipodereparacion',),
        ),
        migrations.AddField(
            model_name='techo',
            name='techo_tipo',
            field=models.ForeignKey(to='reparar.TipoDeTecho'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='techo',
            name='techo_tipo_reparacion',
            field=models.ForeignKey(to='reparar.TReparacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='murosparedes',
            name='mp_tipo_reparacion',
            field=models.ForeignKey(to='reparar.MPReparacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instalacionsanitaria',
            name='inst_sant_tipo_reparacion',
            field=models.ForeignKey(to='reparar.ISReparacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instalacionelectrica',
            name='inst_elect_tipo_reparacion',
            field=models.ForeignKey(to='reparar.IEReparacion'),
            preserve_default=True,
        ),
    ]
