# Generated by Django 2.1.1 on 2020-11-30 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAFA', '0003_auto_20201130_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setlocation',
            old_name='company_X',
            new_name='companyX',
        ),
        migrations.RenameField(
            model_name='setlocation',
            old_name='company_Y',
            new_name='companyY',
        ),
    ]
