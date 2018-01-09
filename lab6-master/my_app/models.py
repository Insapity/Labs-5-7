from django.db import models


class Hotel(models.Model):
        name_hotel = models.CharField(max_length=100)
        price_hotel = models.IntegerField(default=36)


class Country (models.Model):
        cnt_name = models.CharField(max_length=100)
        hotel_name = models.CharField(max_length=100)
