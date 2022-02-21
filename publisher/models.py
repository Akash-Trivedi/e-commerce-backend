# date-created: 17-feb-2022
# usage: all the tables related to the publisher and its products
# calling function:

from django.utils import timezone
from django.db import models


# at the time of registration this table will fill first
class PublisherAuth(models.Model):
    contactId = models.CharField(max_length=10, null=False, primary_key=True)
    password = models.CharField(max_length=64, null=True)


class Publisher(models.Model):
    publisherId = models.AutoField(primary_key=True)
    contactId = models.ForeignKey(PublisherAuth, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=32, null=True)
    lastName = models.CharField(max_length=32, null=True)
    email = models.EmailField(max_length=64, null=True)

    # publisherImage = models.CharField() remaining
    # shopImage = models.CharField() remaining

    dob = models.DateField(null=True)

    registrationDate = models.DateTimeField(null=False, default=timezone.now)

    address = models.CharField(max_length=64, null=True)
    pincode = models.IntegerField(null=False)


class Shop(models.Model):
    publisherShopId = models.AutoField(primary_key=True)
    publisherId = models.ForeignKey(
        Publisher, null=False, on_delete=models.CASCADE)
    shopName = models.CharField(max_length=64, null=False)
    shopPincode = models.CharField(max_length=6, null=False, default='208012')