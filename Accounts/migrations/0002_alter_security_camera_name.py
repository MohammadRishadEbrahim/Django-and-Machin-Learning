# Generated by Django 5.0.6 on 2024-06-23 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='security',
            name='Camera_Name',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.camera'),
        ),
    ]
