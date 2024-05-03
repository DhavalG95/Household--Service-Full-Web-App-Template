from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    fees = models.IntegerField()
    

    def __str__(self):
        return self.name
    
class Login(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    message = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.name