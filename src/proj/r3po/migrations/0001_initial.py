# Generated by Django 2.0.4 on 2018-04-08 15:04

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=200)),
                ('okind', models.CharField(max_length=200, null=True)),
                ('oid', models.CharField(max_length=200, null=True)),
                ('odata', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('ekind', models.CharField(max_length=200, null=True)),
                ('edata', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('user_id', models.IntegerField(null=True)),
                ('tracker', models.CharField(max_length=200, null=True)),
                ('ip', models.CharField(max_length=200, null=True)),
                ('user_agent', models.CharField(max_length=200, null=True)),
                ('visit_id', models.IntegerField(null=True)),
            ],
        ),
    ]
