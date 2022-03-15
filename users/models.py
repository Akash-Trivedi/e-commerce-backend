from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class LocalUser(AbstractUser):
    # primary key
    username = models.CharField(max_length=10, null=False, primary_key=True)
    password = models.CharField(max_length=255, null=False)
    # other details
    first_name = models.CharField(null=True, max_length=150, blank=True)
    last_name = models.CharField(null=True, max_length=150, blank=True)
    email = models.EmailField(null=True, blank=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=255, null=True)
    pincode = models.CharField(max_length=6, null=True)
    ipAddress = models.GenericIPAddressField(default='127.0.0.1')
    browser = models.CharField(
        max_length=255, null=False, default='localhost:chrome')
    homeAddress = models.CharField(max_length=255, null=True, default='-')
    isPublisher = models.BooleanField(null=False)
