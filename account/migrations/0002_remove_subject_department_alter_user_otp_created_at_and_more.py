# Generated by Django 4.1.2 on 2022-11-05 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='department',
        ),
        migrations.AlterField(
            model_name='user',
            name='otp_created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 5, 6, 47, 29, 993283, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='subject',
            name='department',
            field=models.ManyToManyField(to='account.department'),
        ),
    ]