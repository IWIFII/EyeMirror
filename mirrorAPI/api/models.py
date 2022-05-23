from django.db import models


# Create your models here.
class Todolist(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()


class Vision(models.Model):
    id = models.AutoField(primary_key=True)
    leftEye = models.FloatField()
    rightEye = models.FloatField()
    date = models.DateTimeField()
