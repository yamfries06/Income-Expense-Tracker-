from django.db import models
from django.contrib.auth.models import User 
from django.utils.timezone import now 
# Create your models here.

class Expense(models.Model): #allows class to connect to the database
    amount=models.FloatField() #mapping each attribute to one column in the database table
    date=models.DateField(default=now) 
    description=models.TextField()
    owner=models.ForeignKey(to=User, on_delete=models.CASCADE)
    category=models.CharField(max_length=266)
    
    def __str__(self): 
        return self.category #returns a string that represents the object 
    
    class Meta: 
        ordering: ['-date']


class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta: 
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name 

  
