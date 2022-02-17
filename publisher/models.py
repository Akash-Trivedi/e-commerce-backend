# date-created: 17-feb-2022
# usage: all the tables related to the publisher and its products
# calling function:

from django.db import models
from django.contrib.auth.models import AbstractUser


class Publisher(models.Model):
    sellerTypes = {
        'r': 'retail',
        'g': 'godown'
    }

    publisherId = models.BigAutoField()
    contact = models.CharField(max_length=10, null=False)
    firstName = models.CharField(max_length=32, default="")
    lastName = models.CharField(max_length=32, default="")
    email = models.EmailField()
    sellerType = models.TextChoices()
    shopName = models.CharField()

    publisherImage = models.CharField()
    shopImage = models.CharField()

    dob = models.CharField(max_length=32, default="")

    registrationDate = models.models.DateTimeField(
        _(""), auto_now=False, auto_now_add=False)

    address = models.TextField(max_length=64, default="")
    pincode = models.IntegerField(default=0)


class Category(models.Model):
    categoryId = models.BigAutoField()
    categoryName = models.CharField(max_length=32, null=False)


class Product(models.Model):
    size = {
        's': 'Small',
        'm': 'Medium',
        'l': 'Large',
        'xl': 'XL',
        'xxl': 'XXL',
        'xxxl': 'XXXL',
    }
    productId = models.BigAutoField()
    description = models.TextField()
    stock = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    size = models.Choices()
    color = models.Choices()
    # parentCompany=model check for table relations
    # pulisherId=models.
    productImage = models.CharField(default='')
    edition = models.TextChoices()
    discounts = models.IntegerField(default=0)
    category = models.models.ManyToManyField(
        "publisher.models.Category", verbose_name=_(""))

class OrderSummary(models.Model):
    orderId=models.BigAutoField()
    customerId=models.ForeignKey(to, on_delete)
    orderPlaceTime=models.DateTimeField()
    orderDispatchTime=models.DateTimeField()
    orderShippedTime=models.DateTimeField()
    orderDeliveryTime=models.DateTimeField()
    status=models.CharField()
    addressId=models.ForeignKey(to, on_delete)
    pincode=models.IntegerField()