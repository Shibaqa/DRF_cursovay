# Generated by Django 4.2.9 on 2024-07-30 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_alter_habit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(default=datetime.time(15, 56, 2, 139693), verbose_name='Во сколько?'),
        ),
    ]
