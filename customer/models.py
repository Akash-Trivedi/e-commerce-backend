# date-created: 22-feb-2022
# usage: all the tables related to the customer and its related data
# calling function: -

from django.db import models
from django.utils import timezone
from product.models import Product


class CustomerAuth(models.Model):
    # primary key
    contactId = models.CharField(max_length=10, null=False)

    # other details
    password = models.CharField(max_length=255, null=False)


class Customer(models.Model):
    # primary key
    customerId = models.AutoField(primary_key=True)

    # foreign key
    contactId = models.ForeignKey(
        CustomerAuth, on_delete=models.CASCADE)

    # other details
    firstName = models.CharField(max_length=64, null=False)
    lastName = models.CharField(max_length=64,  null=False)
    email = models.EmailField(max_length=255)
    dob = models.DateField()
    registrationDate = models.DateTimeField(default=timezone.now)
    homeAddress = models.CharField(max_length=255, null=True, default='-')
    pincode = models.CharField(max_length=6, null=True)


class Address(models.Model):
    # primary key
    addressId = models.AutoField(primary_key=True)

    # foriegn key
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)

    # other details
    address = models.CharField(max_length=255)
    pincode = models.CharField(max_length=6, null=False)


class Feedback:
    # primary key
    feedbackId = models.AutoField(primary_key=True)

    # foreign key
    customerId = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)

    # other details
    starValue = models.IntegerField(null=False)
    timeStamp = models.DateTimeField(default=timezone.now)
    review = models.TextField(max_length=600)


class OrderSummary(models.Model):
    # primary key
    orderId = models.AutoField(primary_key=True)

    # foreign key
    customerId = models.ForeignKey(
        Customer, on_delete=models.DO_NOTHING, null=True)
    addressId = models.ForeignKey(Address, on_delete=models.DO_NOTHING)

    # unique key
    transactionId = models.CharField(max_length=255, null=False)

    # other details
    orderPlaceTime = models.DateTimeField(timezone.now, null=False)
    orderDispatchTime = models.DateTimeField(null=True)
    orderShippedTime = models.DateTimeField(null=True)
    orderDeliveryTime = models.DateTimeField(null=True)
    paymentTime = models.DateTimeField(null=True)
    status = models.CharField(max_length=10, null=False, default='placed')
    pincode = models.IntegerField()
    paymentOption = models.CharField(max_length=16, null=False)
    paymentDone = models.BooleanField(default=False)
    paymentGateway = models.CharField(max_length=64, null=False)
