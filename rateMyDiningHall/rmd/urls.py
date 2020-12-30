from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addSchool, name='addSchool'),
    path('<str:schoolName>', views.school, name='school2'),
    path('<str:schoolName>/dininghalls', views.dininghalls, name='dininghalls'),
    path('<str:schoolName>/restaurants', views.restaurants, name='restaurants'),
    path('<str:schoolName>/dininghalls/add', views.addDiningHall, name='addDiningHall'),
    path('<str:schoolName>/restaurants/add', views.addRestaurant, name='addRestaurant'),
    path('<str:schoolName>/diningHalls/<str:diningHallName>', views.addDiningHallReview, name='addDHR'),
    path('<str:schoolName>/restaurants/<str:restaurantName>', views.addRestaurantReview, name='addRR')
]