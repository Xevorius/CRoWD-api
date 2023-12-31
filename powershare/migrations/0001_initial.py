# Generated by Django 4.2.5 on 2023-12-04 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PowerShareStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PowerShareOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickupTime', models.DateTimeField()),
                ('returnTime', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pickupStation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pick_up_station', to='powershare.powersharestation')),
                ('returnStation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='return_station', to='powershare.powersharestation')),
            ],
        ),
    ]
