# Generated by Django 4.2.9 on 2024-07-30 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0008_alter_habit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(default=datetime.time(16, 0, 1, 719143), verbose_name='Во сколько?'),
        ),
    ]
