# Generated by Django 5.0.6 on 2024-06-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0002_alter_output_circulating_supply_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='market_cap_rank',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
