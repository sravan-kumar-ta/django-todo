# Generated by Django 3.2.9 on 2021-11-25 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_active',
            new_name='is_complete',
        ),
    ]
