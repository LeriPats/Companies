from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Team(models.Model):
    name = models.CharField(max_length=255)
    floor = models.IntegerField()
    company = models.ForeignKey(
        'org.Company',
        null=True,
        on_delete=models.SET_NULL,
        related_name='teams',
    )

class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    phone_humber = models.CharField(max_length=20)
    birthday = models.DateField(max_length=20)
    email = models.CharField(max_length=20)
    team = models.ForeignKey(
        'org.Team',
        null=True,
        on_delete=models.CASCADE,
        related_name='employees',
    )
