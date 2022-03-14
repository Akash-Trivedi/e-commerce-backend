# date-created: 17-feb-2022
# usage: all the tables related to the publisher and its shops
# calling function: -

from email.policy import default
import ipaddress
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

# at the time of registration this table will fill first


class PublisherAuth(models.Model):
    # primary key
    contactId = models.CharField(max_length=10, null=False, primary_key=True)

    # other details
    password = models.CharField(max_length=255, null=False)
    ipAddress = models.GenericIPAddressField(default='127.0.0.1')
    browser = models.CharField(
        max_length=255, null=False, default='localhost:chrome')
    registrationDate = models.DateTimeField(default=timezone.now)


class Publisher(models.Model):
    # primary key
    publisherId = models.AutoField(primary_key=True)

    # foreign key
    contactId = models.ForeignKey(PublisherAuth, on_delete=models.CASCADE)

    # other details
    firstName = models.CharField(max_length=64, null=True)
    lastName = models.CharField(max_length=64, null=True)
    email = models.EmailField(max_length=255, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=255, null=True)
    pincode = models.CharField(max_length=6, null=True)
    ipAddress = models.GenericIPAddressField(default='127.0.0.1')
    browser = models.CharField(
        max_length=255, null=False, default='localhost:chrome')
    registrationDate = models.DateTimeField(default=timezone.now)


class Shop(models.Model):
    # primary key
    shopId = models.AutoField(primary_key=True)

    # foreign key
    publisherId = models.ForeignKey(
        Publisher, on_delete=models.CASCADE)

    # other details
    name = models.CharField(max_length=64, null=False)
    pincode = models.CharField(max_length=6, null=False)
    address = models.CharField(max_length=255, default='-')
    ipAddress = models.GenericIPAddressField(default='127.0.0.1')
    browser = models.CharField(
        max_length=255, null=False, default='localhost:chrome')
    registrationDate = models.DateTimeField(default=timezone.now)
