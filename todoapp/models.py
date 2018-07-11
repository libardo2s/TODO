from django.db import models


# Create your models here.
class Todo(models.Model):
    task = models.CharField('Task', max_length=60)
    description = models.CharField('Description', max_length=100)
