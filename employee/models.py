from django.db import models

# Create your models here.




class Employee(models.Model):
  name=models.CharField(max_length=80)
  username = models.CharField(max_length=80)
  email=models.EmailField()
  password=models.CharField(max_length=70)
  desig=models.CharField(max_length=80)
  age=models.PositiveIntegerField(default=18)
  salary=models.PositiveIntegerField(default=5000)


  def __str__(self):
    return self.name
