# Generated by Django 5.0.6 on 2024-06-08 07:46

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('price_change', models.FloatField()),
                ('market_cap', models.BigIntegerField()),
                ('market_change', models.IntegerField()),
                ('volume', models.BigIntegerField()),
                ('volume_change', models.FloatField()),
                ('circulating_supply', models.BigIntegerField()),
                ('total_supply', models.BigIntegerField()),
                ('diluted_market_cap', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OfficialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('output', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='official_links', to='coins.output')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('output', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='coins.output')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('output', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socials', to='coins.output')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.CharField(max_length=100)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='coins.job')),
            ],
        ),
        migrations.AddField(
            model_name='output',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='output', to='coins.task'),
        ),
    ]
