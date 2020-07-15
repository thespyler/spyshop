from django.db import models

# Create a User model for the database
class User(models.Model):
	name = models.TextField()
# Create your models here.
	email = models.TextField()
	password = models.TextField()
