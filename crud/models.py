from django.db import models

# Create your models here.


class operation(models.Model):
    sn = models.IntegerField()
    username = models.CharField(max_length=64, null=True, default="none")
    age = models.IntegerField()
