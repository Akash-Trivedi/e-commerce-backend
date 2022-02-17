# date-created: 17-feb-2022
# usage: all the tables related to the publisher and its products
# calling function:

from django.db import models

class Customer(models.Model):
    customerTypes = {
        'r': 'Regular',
        'p': 'premium'
    }

    customerId = models.BigAutoField()
    contact = models.CharField(max_length=10, null=False)
    firstName = models.CharField(max_length=32, default="")
    lastName = models.CharField(max_length=32, default="")
    email = models.EmailField()
    cutomerType = models.TextChoices()
    
    customerImage = models.CharField()

    dob = models.CharField(max_length=32, default="")

    registrationDate = models.models.DateTimeField(
        _(""), auto_now=False, auto_now_add=False)

    address = models.TextField(max_length=64, default="")
    pincode = models.IntegerField(default=0)
    
class Address(models.Model):
    addressId=models.BigAutoField()
    customerId=models.ForeignKey(Customer, on_delete='CASCADE')
    address=models.CharField(max_length=128)
    
class Rating:
    customerId=models.Model()
    count=models.FloatField()
    timeStamp=models.models.DateTimeField(_(""), auto_now=False, auto_now_add=False)
    review=models.CharField(max_length=256)
    product_Id=models.ForeignKey(to, on_delete)
    ipAddress=models.IPAddressField()