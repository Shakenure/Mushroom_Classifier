from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('naiveBayes/', views.naiveBayes),
    path('kmeans/', views.kmeans),
    path('trainNB/', views.trainNB),
    path('predictNB/', views.predictNB),
    path('predictKM/', views.predictKM),
    path('chart/', views.chart),
]