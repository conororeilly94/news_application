from __future__ import unicode_literals
from django.db import models

# Create your models here. DATABASE


class News(models.Model):

    name = models.CharField(max_length=100)
    short_txt = models.TextField()
    body = models.TextField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=12, default='00:00')
    pic = models.TextField()
    picurl = models.TextField(default='-')
    writer = models.CharField(max_length=50)
    catname = models.CharField(max_length=50, default='-')
    catid = models.IntegerField(default=0)
    ocatid = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    tag = models.TextField(default="")



    def __str__(self):
        return self.name