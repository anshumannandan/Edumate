# Generated by Django 4.1.2 on 2022-11-02 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_teacher_pic_alter_user_otp_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='students/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='otp_created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 2, 10, 49, 33, 601394, tzinfo=datetime.timezone.utc)),
        ),
    ]