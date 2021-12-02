from django.db import models
import datetime


# Create your models here.
class Priorities(models.Model):
    priority_id = models.IntegerField()
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    priority = models.ForeignKey(Priorities, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.date.today)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
