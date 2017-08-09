# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
'''
class Person(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)'''
class Size(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    def __str__(self):
       return self.name 
