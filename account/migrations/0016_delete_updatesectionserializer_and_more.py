# Generated by Django 4.1.2 on 2022-11-03 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_merge_20221104_0044'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UpdateSectionSerializer',
        ),
        migrations.AlterField(
            model_name='user',
            name='otp_created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 3, 19, 13, 28, 546261, tzinfo=datetime.timezone.utc)),
        ),
    ]