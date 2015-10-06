# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='имя')),
            ],
            options={
                'verbose_name_plural': 'врачи',
                'ordering': ('name',),
                'verbose_name': 'врача',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('name', models.CharField(max_length=255, verbose_name='Ф.И.О. пациента')),
                ('doctor', models.ForeignKey(related_name='records', verbose_name='Врач', to='doctors.Doctor')),
            ],
            options={
                'verbose_name_plural': 'записи на прием',
                'ordering': ('date', 'time'),
                'verbose_name': 'запись на прием',
            },
        ),
        migrations.AlterUniqueTogether(
            name='record',
            unique_together=set([('date', 'time', 'doctor')]),
        ),
    ]
