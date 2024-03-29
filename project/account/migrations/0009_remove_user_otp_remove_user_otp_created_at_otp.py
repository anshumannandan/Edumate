# Generated by Django 4.1.2 on 2022-11-10 14:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_otp_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='user',
            name='otp_created_at',
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField(blank=True, null=True)),
                ('otp_created_at', models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0, tzinfo=datetime.timezone.utc))),
                ('isexpired', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
