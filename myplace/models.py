from __future__ import unicode_literals

from django.db import models

class Place(models.Model):
      place_name              = models.CharField(max_length=200)
      place_thai_name         = models.CharField(max_length=200)
      place_type              = models.CharField(max_length=200)
class Type(models.Model):
      types                   = models.CharField(max_length=200)
      

