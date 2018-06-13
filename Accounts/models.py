# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class User(request):
    user_name = models.CharField (max_length=100)
    e_mail = models.TextField()
    phone_number = models.CharField (max_length=10)
    image = models.FileField(null=True, blank=True)

class Gears (request):
    gear_type = models.CharField (max_length=100)
    gear_producer = models.CharField (max_length=100)
    gear_name = models.CharField (max_length=100)
    gear_model = models.CharField (max_length=100)
    gear_date = models.CharField (max_length=100)
    gear_state = models.CharField (max_length=100)
    gear_availablity = models.CharField (max_length=100)
    gear_owner = models.CharField (max_length=100)
    gear_price = models.CharField (max_length=100)
    gear_image = models.FileField(null=True, blank=True)
# Create your models here.
class Requested_Gears (request):
    rgear_type = models.CharField (max_length=100)
    rgear_producer = models.CharField (max_length=100)
    rgear_name = models.CharField (max_length=100)
    rgear_model = models.CharField (max_length=100)
    rgear_date = models.CharField (max_length=100)
    rgear_state = models.CharField (max_length=100)
    rgear_availablity = models.CharField (max_length=100)
    rgear_owner = models.CharField (max_length=100)
    rgear_price = models.CharField (max_length=100)
    rgear_image = models.FileField(null=True, blank=True)
