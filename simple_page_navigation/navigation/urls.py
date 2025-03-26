from django.urls import include, path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('services/', views.services),
    path('contact', views.contact),
]