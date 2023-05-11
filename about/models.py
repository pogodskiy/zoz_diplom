from django.db import models

class About(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)


class Contacts(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    telegramm = models.CharField(max_length=15)
