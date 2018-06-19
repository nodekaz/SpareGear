# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

gender_choices=(
    ('', '--'),
    ('F', 'FEMALE'),
    ('M', 'MALE'),
)
type_choices=(
    ('','--'),
    ('car','car gears'),
    ('home','home gears'),
    ('electroics', 'electronic gears'),
    ('computers', 'computer gears'),
    ('office', 'office equipment gears'),
    ('medical', 'medical equipment gears'),
)


class User(models.Model):
    user_name = models.CharField (verbose_name="اسم المستخدم",max_length=100)
    gender = models.CharField(verbose_name="الجنس", choices= gender_choices)
    e_mail = models.EmailField (verbose_name="الايميل")
    phone_number = models.IntegerField (verbose_name="الجوال", max_length=10)
    image = models.FileField(verbose_name=" الصورة الشخصية (إن وجدت)",null=True, blank=True)

class Gear (models.Model):
    gear_type = models.CharField (verbose_name=" نوع القطعة",max_length=100, choices=type_choices)
    gear_producer = models.CharField (verbose_name="الشركة المصنعة",max_length=100)
    gear_name = models.CharField (verbose_name="اسم القطعة",max_length=100)
    gear_model = models.CharField (verbose_name="موديل القطعة",max_length=100)
    gear_date = models.CharField (verbose_name="تاريخ توفر القطعة",max_length=100)
    gear_quality = models.CharField (verbose_name= "جودةالقطعة",max_length=100)
    gear_availablity = models.BooleanField(verbose_name="توفر القطعة" ,max_length=100)
    gear_owner = models.CharField (verbose_name="مالك القطعة",max_length=100)
    gear_price = models.CharField (verbose_name="سعر القطعة" ,max_length=100)
    gear_image = models.FileField(verbose_name= "صورة القطعة",null=True, blank=True)

class Requested_Gear (models.Model):
    rgear_type = models.CharField (verbose_name=" نوع القطعة المرغوبة" ,max_length=100, choices= type_choices)
    rgear_producer = models.CharField (verbose_name="الشركة المصنعة " ,max_length=100)
    rgear_name = models.CharField (verbose_name= " اسم القطعة",max_length=100)
    rgear_model = models.CharField (verbose_name="موديل القطعة" ,max_length=100)
    rgear_date = models.CharField (verbose_name="تاريخ الاستعلام" ,max_length=100)
    rgear_state = models.CharField (verbose_name="جودة القطعة المرغوبة" ,max_length=100)
    rgear_availablity = models.CharField (verbose_name=" حالة الاستعلام" ,max_length=100)
    rgear_requester = models.CharField (verbose_name=" المستعلم عن القطعة" ,max_length=100)
    rgear_price = models.CharField (verbose_name=" سعر القطعة المرغوبة" ,max_length=100)
    rgear_image = models.FileField(verbose_name="صورة القطعة المرغوبة (إن وجدت)" ,null=True, blank=True)
# Create your models here.
