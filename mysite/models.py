from django.db import models


class Register(models.Model):
    FName = models.CharField(max_length=20)
    LName = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    Password = models.IntegerField()

    def __str__(self):
        return self.FName   
            
    
class Contact(models.Model):
    Name =models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    Phone=models.CharField(max_length=12)
    Message=models.TextField()
     

        
