from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save

import os

class Specialization(models.Model):
    name = models.CharField(max_length=30)


class Clinic(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact_no = models.IntegerField() 
    address = models.CharField(max_length=500)
    website = models.CharField(max_length=50)


class DoctorSeeker(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return u"%s %s" % (self.name, self.email)

    def create_doctorSeeker_profile(sender, instance, created, **kwargs):
        if created:
            DoctorSeeker.objects.create(user=instance)

    post_save.connect(create_doctorSeeker_profile, sender=User)


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    specializations = models.ManyToManyField(Specialization)
    clinic = models.ManyToManyField(Clinic)
    seekers = models.ManyToManyField(DoctorSeeker, through='Review')
    
    def __unicode__(self):
      return u"%s %s" % (self.name, self.email)


class Review(models.Model):
    comment = models.CharField(max_length=500)
    date = models.DateField()
    doctor = models.ForeignKey(Doctor)
    doctor_seeker = models.ForeignKey(DoctorSeeker)