from django.urls import path
from . import views
from .views import CustomSignupView

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/reset-picture/', views.reset_profile_picture, name='reset_profile_picture'),
    path('reservations/', views.reservations, name='reservations'),
    path('orders/', views.orders, name='orders'),
    path('comments/', views.comments, name='comments'),
    path('contact/', views.contact, name='contact'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]
