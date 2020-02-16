from django.db import models
from django.contrib.auth.models import User
from shop.models import Products
# Create your models here.

class Cart(models.Model):

	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Products,on_delete=models.CASCADE,default=1)
	quantity=models.IntegerField(default=1)



