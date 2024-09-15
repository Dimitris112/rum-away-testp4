from django.urls import path
from . import views
from .views import (
    index, reservations, profile, reset_profile_picture,
    orders, comments, contact, event_list, event_detail, menu,
    CustomSignupView
)

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('profile/reset-picture/', reset_profile_picture, name='reset_profile_picture'),
    path('reservations/', reservations, name='reservations'),
    path('orders/', orders, name='orders'),
    path('comments/', comments, name='comments'),
    path('contact/', contact, name='contact'),
    path('events/', event_list, name='event_list'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('menu/', menu, name='menu'),
]
