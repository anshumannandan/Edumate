# Generated by Django 4.1.2 on 2022-11-02 11:57

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_student_pic_alter_user_otp_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='blood_group',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='father_phone',
            field=models.BigIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AddField(
            model_name='student',
            name='mother_phone',
            field=models.BigIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AddField(
            model_name='student',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_phone',
            field=models.BigIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='students/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='otp_created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 2, 11, 56, 14, 153497, tzinfo=datetime.timezone.utc)),
        ),
    ]