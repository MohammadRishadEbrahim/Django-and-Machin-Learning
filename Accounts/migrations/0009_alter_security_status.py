# Generated by Django 5.0.6 on 2024-06-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_alter_security_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='security',
            name='Status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('No Active', 'No Active')], max_length=50, null=True),
        ),
    ]
