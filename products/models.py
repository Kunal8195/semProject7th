from django.db import models

# Create your models here.

class product(models.Model):
       productname=models.CharField(max_length=100)
       producttype=models.CharField(max_length=50)
       availability=models.CharField(max_length=20)
       condition= models.CharField(max_length=20)
       brand=models.CharField(max_length=100)
       price=models.IntegerField()
       image=models.FileField()
       featured=models.IntegerField()
       trending=models.IntegerField()

class category(models.Model):
	productname=models.CharField(max_length=100)
	producttype=models.CharField(max_length=50)
	availability=models.CharField(max_length=20)
	condition= models.CharField(max_length=20)
	brand=models.CharField(max_length=100)
	price=models.IntegerField()
	image=models.FileField()
	civil=models.IntegerField()
	csit=models.IntegerField()
	mechanical=models.IntegerField()
	electrical=models.IntegerField()
	electronics=models.IntegerField()