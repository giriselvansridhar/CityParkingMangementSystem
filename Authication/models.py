from django.db import models

class User(models.Model):
    number = models.CharField(max_length=10)
    password = models.CharField(max_length=6)

    def __str__(self):
        return self.number
    

    
