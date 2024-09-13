from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('reservations/', views.reservations, name='reservations'),
    path('orders/', views.orders, name='orders'),
    path('comments/', views.comments, name='comments'),
]
