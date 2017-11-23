from django.db import models

# Create your models here.

class product(models.Model):
       productname=models.CharField(max_length=20)
       producttype=models.CharField(max_length=20)
       availability=models.CharField(max_length=20)
       condition= models.CharField(max_length=20)
       brand=models.CharField(max_length=20)
       price=models.IntegerField()
       image=models.FileField() 
      
