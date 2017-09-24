from django.db import models


# Create your models here.
class NewAccount(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    drowssap = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=30)
    photograph = models.CharField(max_length=1000)
