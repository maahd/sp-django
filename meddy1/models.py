from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save

import os

class Specialization(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Clinic(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField() #required = False
    contact_no = models.IntegerField() 
    address = models.CharField(max_length=500)
    website = models.CharField(max_length=50)

    def __unicode__(self):
        return u"%s %s" % (self.name, self.email)


class DoctorSeeker(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    user = models.OneToOneField(User, unique=True)

    def __unicode__(self):
        return u"%s %s" % (self.name, self.email)

def create_seeker_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = DoctorSeeker.objects.get_or_create(user=instance)
        
post_save.connect(create_seeker_profile, sender=User)


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    # specializations = models.ManyToManyField(Specialization)
    specialization = models.ForeignKey(Specialization)
    # clinic = models.ManyToManyField(Clinic)
    clinic = models.ForeignKey(Clinic)
    seekers = models.ManyToManyField(DoctorSeeker, through='Review')
    
    def __unicode__(self):
      return u"%s %s" % (self.name, self.email)


class Review(models.Model):
    comment = models.CharField(max_length=500)
    date = models.DateField()
    doctor = models.ForeignKey(Doctor)
    doctor_seeker = models.ForeignKey(DoctorSeeker)

    def __unicode__(self):
        return u"%s %s" % (self.date, self.comment, Self.doctor_seeker, )