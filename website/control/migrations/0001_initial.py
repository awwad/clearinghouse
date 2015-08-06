# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionLogEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('function_name', models.CharField(max_length=50, verbose_name=b'Function type', db_index=True)),
                ('second_arg', models.CharField(max_length=50, null=True, verbose_name=b'Second arg')),
                ('third_arg', models.CharField(max_length=50, null=True, verbose_name=b'Third arg')),
                ('was_successful', models.BooleanField(db_index=True)),
                ('message', models.CharField(max_length=1024, null=True, verbose_name=b'Message')),
                ('vessel_count', models.IntegerField(null=True, verbose_name=b'Vessel count', db_index=True)),
                ('date_started', models.DateTimeField(verbose_name=b'Date started', db_index=True)),
                ('completion_time', models.FloatField(verbose_name=b'Completion time (seconds)', db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActionLogVesselDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_address', models.CharField(max_length=100, verbose_name=b'Node address', db_index=True)),
                ('node_port', models.IntegerField(verbose_name=b'Node port', db_index=True)),
                ('vessel_name', models.CharField(max_length=50, verbose_name=b'Vessel name', db_index=True)),
                ('event', models.ForeignKey(to='control.ActionLogEvent')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(db_index=True, max_length=100, verbose_name=b'Donation status', blank=True)),
                ('resource_description_text', models.TextField(verbose_name=b'Resource description')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date added to DB', db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name=b'Date modified in DB', db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('researcher_name', models.CharField(max_length=30)),
                ('researcher_email', models.EmailField(max_length=254)),
                ('researcher_address', models.CharField(max_length=64)),
                ('irb_officer_name', models.CharField(max_length=30)),
                ('irb_officer_email', models.EmailField(max_length=254)),
                ('goal', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Experiment info',
            },
        ),
        migrations.CreateModel(
            name='ExperimentSensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('frequency', models.IntegerField()),
                ('usage_policy', models.CharField(max_length=512)),
                ('downloadable', models.BooleanField(default=True)),
                ('experiment', models.ForeignKey(to='control.Experiment')),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentSensorAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precision', models.IntegerField()),
                ('experiment_id', models.ForeignKey(to='control.Experiment')),
                ('experiment_sensor_id', models.ForeignKey(to='control.ExperimentSensor')),
            ],
        ),
        migrations.CreateModel(
            name='GeniUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('usable_vessel_port', models.IntegerField(verbose_name=b"GeniUser's vessel port")),
                ('affiliation', models.CharField(max_length=200, verbose_name=b'Affiliation')),
                ('user_pubkey', models.CharField(max_length=2048, verbose_name=b"GeniUser's public key")),
                ('user_privkey', models.CharField(max_length=4096, null=True, verbose_name=b"GeniUser's private key [!]")),
                ('api_key', models.CharField(max_length=100, verbose_name=b'API key', db_index=True)),
                ('donor_pubkey', models.CharField(max_length=2048, verbose_name=b'Donor public Key')),
                ('free_vessel_credits', models.IntegerField(verbose_name=b'Free (gratis) vessel credits', db_index=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date added to DB', db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name=b'Date modified in DB', db_index=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_identifier', models.CharField(max_length=2048, verbose_name=b'Node identifier')),
                ('last_known_ip', models.CharField(max_length=100, verbose_name=b'Last known nodemanager IP address or NAT string', db_index=True)),
                ('last_known_port', models.IntegerField(verbose_name=b'Last known nodemanager port', db_index=True)),
                ('last_known_version', models.CharField(db_index=True, max_length=64, verbose_name=b'Last known version', blank=True)),
                ('date_last_contacted', models.DateTimeField(auto_now_add=True, verbose_name=b'Last date successfully contacted', db_index=True)),
                ('is_active', models.BooleanField(db_index=True)),
                ('is_broken', models.BooleanField(db_index=True)),
                ('owner_pubkey', models.CharField(max_length=2048, verbose_name=b'Owner public key')),
                ('extra_vessel_name', models.CharField(max_length=8, verbose_name=b'Extra-vessel name', db_index=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date added to DB', db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name=b'Date modified in DB', db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SensorAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('sensor', models.ForeignKey(to='control.Sensor')),
            ],
        ),
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Vessel name', db_index=True)),
                ('date_acquired', models.DateTimeField(null=True, verbose_name=b'Date acquired', db_index=True)),
                ('date_expires', models.DateTimeField(null=True, verbose_name=b'Date that acquisition expires', db_index=True)),
                ('is_dirty', models.BooleanField(db_index=True)),
                ('user_keys_in_sync', models.BooleanField(db_index=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date added to DB', db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name=b'Date modified in DB', db_index=True)),
                ('acquired_by_user', models.ForeignKey(to='control.GeniUser', null=True)),
                ('node', models.ForeignKey(to='control.Node')),
            ],
        ),
        migrations.CreateModel(
            name='VesselPort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('port', models.IntegerField(verbose_name=b'Port', db_index=True)),
                ('vessel', models.ForeignKey(to='control.Vessel')),
            ],
        ),
        migrations.CreateModel(
            name='VesselUserAccessMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date added to DB', db_index=True)),
                ('user', models.ForeignKey(to='control.GeniUser')),
                ('vessel', models.ForeignKey(to='control.Vessel')),
            ],
        ),
        migrations.AddField(
            model_name='experimentsensorattribute',
            name='sensor_attribute_id',
            field=models.ForeignKey(to='control.SensorAttribute'),
        ),
        migrations.AddField(
            model_name='experimentsensor',
            name='sensor',
            field=models.ForeignKey(to='control.Sensor'),
        ),
        migrations.AddField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(to='control.GeniUser'),
        ),
        migrations.AddField(
            model_name='donation',
            name='node',
            field=models.ForeignKey(to='control.Node'),
        ),
        migrations.AddField(
            model_name='actionlogvesseldetails',
            name='node',
            field=models.ForeignKey(to='control.Node'),
        ),
        migrations.AddField(
            model_name='actionlogevent',
            name='user',
            field=models.ForeignKey(to='control.GeniUser', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='vesseluseraccessmap',
            unique_together=set([('vessel', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='vesselport',
            unique_together=set([('vessel', 'port')]),
        ),
        migrations.AlterUniqueTogether(
            name='vessel',
            unique_together=set([('node', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='donation',
            unique_together=set([('node', 'donor')]),
        ),
    ]
