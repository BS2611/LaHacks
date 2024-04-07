
from django.contrib import admin
from django.urls import path
from backend import views
urlpatterns = [
    path('login/', views.my_view),
    path('recipie/',views.getRecipe),
]
