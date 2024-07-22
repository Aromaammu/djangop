from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=500)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=5000)
