# Generated by Django 2.1.1 on 2020-11-30 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAFA', '0005_remove_location_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setlocation',
            old_name='homxY',
            new_name='homeY',
        ),
    ]
