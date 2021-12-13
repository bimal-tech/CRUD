from django.db import models

# Create your models here.


class operation(models.Model):
    rn = models.IntegerField()
    username = models.CharField(max_length=64, null=True, default="none")
    age = models.IntegerField()
