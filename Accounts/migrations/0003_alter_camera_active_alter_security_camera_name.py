# Generated by Django 5.0.6 on 2024-06-23 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_alter_security_camera_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='Active',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.security'),
        ),
        migrations.AlterField(
            model_name='security',
            name='Camera_Name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.camera'),
        ),
    ]
