# Generated by Django 3.2.9 on 2021-11-27 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_rename_is_active_task_is_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todo_app.priority'),
        ),
    ]
