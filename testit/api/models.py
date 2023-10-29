from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Printer(models.Model):
    type = models.CharField(max_length=160)
    fillament_color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    speed = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank = True, null = True)
    price = models.FloatField()
    latitude = models.DecimalField(max_digits=10, decimal_places=4)
    longitude = models.DecimalField(max_digits=10, decimal_places=4)
    
    def __str__(self):
        return self.type
    
class Task(models.Model):
    file = models.CharField(max_length=256)
    fillament_color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    printer = models.ForeignKey(Printer, on_delete = models.CASCADE, blank = True, null = True)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank = True, null = True)
    price = models.FloatField()
    
    def __str__(self):
        return self.file