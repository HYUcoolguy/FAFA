# Generated by Django 2.1.1 on 2020-12-01 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FAFA', '0004_auto_20201202_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='user',
        ),
        migrations.AddField(
            model_name='alert',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FAFA.User'),
            preserve_default=False,
        ),
    ]
