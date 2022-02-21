# date-created: 19-feb-2022
# usage: contains all the models/tables related to product app
# calling function:

from django.db import models
from django.forms import CharField


tagChoices = [
    ('Electronics', 'Electronics'),
    ('Sports', 'Sports'),
    ('Cooking Utensiles', 'Cooking Utensils'),
]


class Tag(models.Model):
    tagId = models.AutoField(primary_key=True)
    tagName = models.CharField(choices=tagChoices, max_length=64, null=False)

    def __str__(self):
        return self.tagName


class Company(models.Model):
    companyId = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=64, null=False, unique=True)


size = {
    'none': 'none',
    's': 'Small',
    'm': 'Medium',
    'l': 'Large',
    'xl': 'XL',
    'xxl': 'XXL',
    'xxxl': 'XXXL',
}

# generalized model for product, differentiate by tagId


class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    description = models.CharField(max_length=32)
    stock = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    size = models.CharField(max_length=8, null=True, default='-')
    color = models.CharField(max_length=32)
    company = models.ForeignKey(Company, null=False, on_delete=models.CASCADE)
    edition = models.CharField(max_length=32, default='-')
    discounts = models.IntegerField(default=0)
    tagId = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)


# class OrderSummary(models.Model):
#     orderId = models.BigAutoField()
#     customerId = models.ForeignKey(to, on_delete)
#     orderPlaceTime = models.DateTimeField()
#     orderDispatchTime = models.DateTimeField()
#     orderShippedTime = models.DateTimeField()
#     orderDeliveryTime = models.DateTimeField()
#     status = models.CharField()
#     addressId = models.ForeignKey(to, on_delete)
#     pincode = models.IntegerField()
