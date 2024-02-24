from django.contrib import admin
from django.urls import path
from w_app import views

urlpatterns = [
    path('', views.index),
    path('notes/', views.notes, name='notes'),
    path('about/', views.about),
    path('contact/', views.contact),
    path('update/', views.profile_update),
    path('logout/', views.userlogout),
    path('otpverify/', views.otpverify, name='otpverify'),
]