from datetime import date
import numbers
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    number=models.CharField(max_length=12)
    cont=models.TextField()
    date=models.DateField()
