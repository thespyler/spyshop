from django.db import models


class User(models.Model):
	name = models.TextField()
# Create your models here.
	email = models.TextField()
	password = models.TextField()
