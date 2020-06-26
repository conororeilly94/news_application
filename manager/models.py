from __future__ import unicode_literals
from django.db import models

# Create your models here. DATABASE


class Manager(models.Model):
    
    name = models.CharField(max_length=30)
    utxt = models.TextField()
    email = models.TextField(default="")


    def __str__(self):
        return self.set_name