# Generated by Django 5.0.6 on 2024-06-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_alter_security_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='security',
            name='Status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
