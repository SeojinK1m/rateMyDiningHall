from django.db import models
from django.core.validators import RegexValidator
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=128, validators=[alphanumeric])
    urlName = models.CharField(max_length=128)

class diningHall(models.Model):
    name = models.CharField(max_length=128, validators=[alphanumeric])
    urlName = models.CharField(max_length=128)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Restaurant(models.Model):
    name = models.CharField(max_length=128, validators=[alphanumeric])
    urlName = models.CharField(max_length=128)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class diningHallReview(models.Model):
    rating = models.FloatField()
    diningHall = models.ForeignKey(diningHall, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000)

class restaurantReview(models.Model):
    rating = models.FloatField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000)

