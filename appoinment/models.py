from django.db import models

# Create your models here.
class Appoinment(models.Models):
    name=models.CharField(max_length=50)
    phone=models.IntegerField(max_length=15)
    message=models.TextField(max_length=2000)

