from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
