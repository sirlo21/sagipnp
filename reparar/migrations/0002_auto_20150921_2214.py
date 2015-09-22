# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levantamiento', '0001_initial'),
        ('reparar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeredaExterior',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ve_descripcion', models.TextField()),
                ('ve_numero_unidad_medida', models.PositiveIntegerField(default=0, max_length=20)),
                ('ve_dimensiones', models.CharField(max_length=150)),
                ('ve_precio_unitario', models.PositiveIntegerField(default=0)),
                ('ve_precio_total_referencial', models.PositiveIntegerField(default=0)),
                ('ve_tiempo_ejecucion', models.PositiveIntegerField()),
                ('ve_img', models.ImageField(upload_to=b'images/')),
                ('ve_doc', models.FileField(upload_to=b'docs/')),
                ('ve_observaciones', models.TextField(null=True, blank=True)),
                ('ve_vigente', models.BooleanField(default=True)),
                ('ve_pub_data', models.DateTimeField(auto_now=True)),
                ('ve_estado_ejecucion', models.ForeignKey(to='reparar.EstadoDeEjecucion')),
                ('ve_form', models.ForeignKey(related_name='veredas_exteriores', to='levantamiento.Levantamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VEReparacion',
            fields=[
                ('tipodereparacion_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='reparar.TipoDeReparacion')),
            ],
            options={
            },
            bases=('reparar.tipodereparacion',),
        ),
        migrations.AddField(
            model_name='veredaexterior',
            name='ve_tipo_reparacion',
            field=models.ForeignKey(to='reparar.VEReparacion'),
            preserve_default=True,
        ),
    ]
