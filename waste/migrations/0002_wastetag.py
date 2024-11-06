# Generated by Django 5.0.6 on 2024-11-06 01:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WasteTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('waste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waste.waste')),
            ],
        ),
    ]
