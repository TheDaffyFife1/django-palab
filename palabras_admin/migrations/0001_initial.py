# Generated by Django 4.2.11 on 2024-04-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extraccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_row_id', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('received_timestamp', models.DateTimeField(blank=True, null=True)),
                ('text_data', models.TextField(blank=True, null=True)),
                ('from_me', models.IntegerField(blank=True, null=True)),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('verified_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cliente', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(blank=True, max_length=255, null=True)),
                ('municipio', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'extraccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Extraccion2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_row_id', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('received_timestamp', models.DateTimeField(blank=True, null=True)),
                ('text_data', models.TextField(blank=True, null=True)),
                ('from_me', models.IntegerField(blank=True, null=True)),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('verified_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cliente', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'extraccion2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Extraccion3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_row_id', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('received_timestamp', models.DateTimeField(blank=True, null=True)),
                ('text_data', models.TextField(blank=True, null=True)),
                ('from_me', models.IntegerField(blank=True, null=True)),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('verified_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cliente', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(blank=True, max_length=255, null=True)),
                ('municipio', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'extraccion3',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Extraccion4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_row_id', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('received_timestamp', models.DateTimeField(blank=True, null=True)),
                ('text_data', models.TextField(blank=True, null=True)),
                ('from_me', models.IntegerField(blank=True, null=True)),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('number2', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('verified_name', models.CharField(blank=True, max_length=255, null=True)),
                ('server', models.CharField(blank=True, max_length=255, null=True)),
                ('device', models.CharField(blank=True, max_length=255, null=True)),
                ('group_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cliente', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(blank=True, max_length=255, null=True)),
                ('municipio', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'extraccion4',
                'managed': False,
            },
        ),
    ]