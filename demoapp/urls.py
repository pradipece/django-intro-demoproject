from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hi, name="hi"),
    path('watch/', views.watch, name="watch"),
    path('', views.home, name="website"),
]
