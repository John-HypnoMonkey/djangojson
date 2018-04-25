from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    country = models.ForeignKey(Country, related_name='Countries',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.name
