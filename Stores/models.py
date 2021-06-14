from django.db import models
from datetime import datetime

class Jean(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name

class Polo(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name

class Shirts(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name

class Suites(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name

class T_shirts(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name


