from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    mobile =  models.CharField(max_length=8)
    note = models.TextField()
    
    def __str__(self):
        return self.name


class User(models.Model):
    # username = models.CharField(max_length=50)
    # email = models.EmailField(max_length=50, unique=True)
    # password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
