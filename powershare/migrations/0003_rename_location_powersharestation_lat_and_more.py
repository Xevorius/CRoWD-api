# Generated by Django 4.2.5 on 2023-12-05 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powershare', '0002_powershareorder_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='powersharestation',
            old_name='location',
            new_name='lat',
        ),
        migrations.AddField(
            model_name='powersharestation',
            name='lon',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
