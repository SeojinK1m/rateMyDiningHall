from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('write', views.write, name='write'),
    path('add', views.addSchool, name='addSchool'),
    path('<str:schoolName>', views.school, name='school')
]