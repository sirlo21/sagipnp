# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('media_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='media_objects.Media')),
                ('img', models.ImageField(upload_to=b'images/')),
            ],
            options={
            },
            bases=('media_objects.media',),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('media_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='media_objects.Media')),
                ('doc', models.FileField(upload_to=b'docs/')),
            ],
            options={
            },
            bases=('media_objects.media',),
        ),
        migrations.AddField(
            model_name='media',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType'),
            preserve_default=True,
        ),
    ]
