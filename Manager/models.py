from django.db import models

# Create your models here.
class Cart(models.Model):
	product = models.TextField(max_length=200)
	price = models.IntegerField()

	