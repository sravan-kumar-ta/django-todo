# Generated by Django 3.2.9 on 2021-11-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_auto_20211127_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(max_length=20),
        ),
    ]
