from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ToDoDetails(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    todo_data = models.CharField(max_length=225)
