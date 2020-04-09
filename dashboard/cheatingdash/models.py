from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)


    def __str__(self):
        return self.name