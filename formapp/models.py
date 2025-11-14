from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Student(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be exactly 10 digits." )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=10 ,validators=[phone_regex], unique=True) 
    address = models.CharField(max_length=250)
