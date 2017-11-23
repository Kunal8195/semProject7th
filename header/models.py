from django.db import models

# Create your models here.

class Customers(models.Model):
     customernumber = models.CharField(max_length = 10)
     customername   = models.CharField(max_length = 100)
     contactlastname = models.CharField(max_length = 100)
     contactfirstname = models.CharField(max_length =100)
     phone = models.CharField(max_length =10)

class Contact(models.Model):
     customer = models.ForeignKey(Customers,on_delete = models.CASCADE)
     address = models.CharField(max_length = 100)
     city = models.CharField(max_length = 20)
     state = models.CharField(max_length = 15)
     country = models.CharField(max_length = 14) 

class Customer(models.Model):
     name = models.CharField(max_length= 100)  
     email = models.CharField(max_length = 100)
     password = models.CharField(max_length = 10)


