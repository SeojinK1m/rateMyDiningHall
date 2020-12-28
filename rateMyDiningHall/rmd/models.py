from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=128)
    urlName = models.CharField(max_length=128)

class diningHall(models.Model):
    name = models.CharField(max_length=128)
    urlName = models.CharField(max_length=128)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    urlName = models.CharField(max_length=128)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class diningHallReview(models.Model):
    RATINGS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]
    rating = models.IntegerField(choices=RATINGS)
    diningHall = models.ForeignKey(diningHall, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000)

class restaurantReview(models.Model):
    RATINGS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]
    rating = models.IntegerField(choices=RATINGS)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000)
