from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    email = models.EmailField('Email address', unique=True)
    phone_number = models.CharField('Phone number', max_length=13)
    image = models.ImageField(upload_to='user/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
