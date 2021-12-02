from django.contrib import admin
from .models import Task, Priorities

# Register your models here.
admin.site.register(Task)
admin.site.register(Priorities)
