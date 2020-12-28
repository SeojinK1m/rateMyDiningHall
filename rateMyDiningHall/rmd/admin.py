from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(School)
admin.site.register(diningHall)
admin.site.register(Restaurant)
admin.site.register(diningHallReview)
admin.site.register(restaurantReview)