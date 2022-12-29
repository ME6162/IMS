from django.db import models


class Institute(models.Model):
    id = models.SmallAutoField(primary_key=True)
    fullname = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    admin = models.IntegerField()


class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=50)
