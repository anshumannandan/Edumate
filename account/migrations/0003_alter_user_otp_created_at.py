# Generated by Django 4.1.2 on 2022-10-31 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp_created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 31, 16, 0, 55, 619584, tzinfo=datetime.timezone.utc)),
        ),
    ]