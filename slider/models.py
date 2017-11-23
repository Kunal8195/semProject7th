from django.db import models

# Create your models here.

class slider(models.Model):
	image=models.CharField(max_length=100)
	
