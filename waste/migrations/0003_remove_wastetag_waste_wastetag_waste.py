# Generated by Django 5.0.6 on 2024-11-06 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0002_wastetag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wastetag',
            name='waste',
        ),
        migrations.AddField(
            model_name='wastetag',
            name='waste',
            field=models.ManyToManyField(related_name='tags', to='waste.waste'),
        ),
    ]