# Generated by Django 4.2.5 on 2023-12-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powershare', '0003_rename_location_powersharestation_lat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powersharestation',
            name='lat',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='powersharestation',
            name='lon',
            field=models.FloatField(max_length=100),
        ),
    ]
