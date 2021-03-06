# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from core.models import Documents
from core.preset_choices import VEHICLE_STATUS
# Create your models here.

class Person(models.Model):
    """
        Class base to inherit its fields to another model related with a Person.
    """

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=120)
    picture = models.ImageField(upload_to='files/pictures')

    @property
    def full_name(self):
        """Returns person full name."""
        return '%s %s' % (self.first_name, self.last_name)


class Driver(Person):
    """
        Define a person who can drive a taxi.
    """

    related_documents = models.ManyToManyField(Documents)

    def __str__(self):
        return self.full_name

class VehicleMaker(models.Model):
    """
        Vehicle Makers eg: Toyota, Mitsubishi, etc.
    """

    title = models.CharField(max_length=100)


class VehicleModel(models.Model):
    """
        Model: eg, Corolla, Lancer, etc.
    """

    title = models.CharField(max_length=100)
    made = models.ForeignKey('VehicleMaker', on_delete=models.CASCADE)


class Vehicle(models.Model):
    """
        Describe a taxi.
    """

    register = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    year = models.CharField(max_length=8)
    status = models.CharField(max_length=1, choices=VEHICLE_STATUS)
    made = models.ForeignKey('VehicleMaker', on_delete=models.CASCADE)
    model = models.ForeignKey('VehicleModel', on_delete=models.CASCADE)
