from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('write', views.write, name='write'),
    path('add', views.addSchool, name='addSchool'),
    path('write/<str:schoolName>', views.school, name='school'),
    path('<str:schoolName>', views.school, name='school2')
]