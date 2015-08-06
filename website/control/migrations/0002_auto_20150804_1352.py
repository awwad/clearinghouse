# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experimentsensorattribute',
            old_name='experiment_id',
            new_name='experiment',
        ),
        migrations.RenameField(
            model_name='experimentsensorattribute',
            old_name='experiment_sensor_id',
            new_name='experiment_sensor',
        ),
        migrations.RenameField(
            model_name='experimentsensorattribute',
            old_name='sensor_attribute_id',
            new_name='sensor_attribute',
        ),
    ]
