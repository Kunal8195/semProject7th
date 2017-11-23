from django.db import models

# Create your models here.

class cart_items(models.Model):
	product = models.IntegerField(0)
	price=models.IntegerField()
	productname=models.CharField(max_length=20)
	image=models.FileField()
