from django.db import models
import datetime


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    priority = models.CharField(max_length=20)
    created_at = models.DateField(default=datetime.date.today)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
