# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubigeo', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CComisaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clase', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DivisionPolicial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('division', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('especialidad', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grado', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instalacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instalacion', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Levantamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inicio', models.DateField()),
                ('termino', models.DateField()),
                ('coordinador_equipo', models.CharField(max_length=300)),
                ('integrante_1', models.CharField(max_length=300)),
                ('integrante_2', models.CharField(max_length=300)),
                ('integrante_3', models.CharField(max_length=300)),
                ('centro_poblado', models.CharField(max_length=1000)),
                ('nombre_instalacion', models.CharField(max_length=300)),
                ('direccion_instalacion', models.CharField(max_length=500)),
                ('ejecutando_mejoras_mantenimiento', models.NullBooleanField()),
                ('monto', models.IntegerField(default=0, null=True, blank=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=8)),
                ('telefono_fijo_comisaria', models.CharField(max_length=7)),
                ('celular_rpc_comisaria', models.CharField(max_length=9)),
                ('celular_rpm_comisaria', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=75)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(related_name='formularios', blank=True, to='levantamiento.Category', null=True)),
                ('clase_comisaria', models.ForeignKey(related_name='formularios', blank=True, to='levantamiento.CComisaria', null=True)),
                ('division', models.ForeignKey(related_name='formularios', blank=True, to='levantamiento.DivisionPolicial', null=True)),
                ('especialidad', models.ForeignKey(related_name='formularios', blank=True, to='levantamiento.Especialidad', null=True)),
                ('grado', models.ForeignKey(related_name='formularios', blank=True, to='levantamiento.Grado', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegionPolicial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SituacionLegal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('situacion', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TComisaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnidadEjecutora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidad', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='levantamiento',
            name='region_policial',
            field=models.ForeignKey(related_name='formularios', blank=True, to='levantamiento.RegionPolicial', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='levantamiento',
            name='situacion_del_predio',
            field=models.ForeignKey(related_name='formularios', blank=True, to='levantamiento.SituacionLegal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='levantamiento',
            name='tipo_comisaria',
            field=models.ForeignKey(related_name='formularios', blank=True, to='levantamiento.TComisaria', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='levantamiento',
            name='tipo_instalacion',
            field=models.ForeignKey(related_name='formulario', to='levantamiento.Instalacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='levantamiento',
            name='ubigeo',
            field=models.ForeignKey(related_name='formularios', to='ubigeo.Ubigeo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='levantamiento',
            name='unidad_ejecutora',
            field=models.ForeignKey(related_name='formularios', to='levantamiento.UnidadEjecutora'),
            preserve_default=True,
        ),
    ]
