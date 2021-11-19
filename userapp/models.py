import datetime

from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    salary = models.CharField(max_length=10)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Persone(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    Is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=60)
    publication = models.ManyToManyField(Persone)
    # Post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
