from django.db import models


# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task
