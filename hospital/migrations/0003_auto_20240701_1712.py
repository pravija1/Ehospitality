# Generated by Django 3.0.5 on 2024-07-01 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_patientprescribedetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientprescribedetails',
            old_name='medications',
            new_name='medication',
        ),
    ]
