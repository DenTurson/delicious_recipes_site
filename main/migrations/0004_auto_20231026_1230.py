# Generated by Django 3.2.22 on 2023-10-26 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_dish_dish_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='dish_cooking_process',
            field=models.TextField(default='The process of cooking you delicious dish:'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_published',
            field=models.DateField(default=datetime.datetime(2023, 10, 26, 12, 30, 34, 450065), verbose_name='date published'),
        ),
    ]
