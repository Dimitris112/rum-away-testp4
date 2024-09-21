from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .api import user_profile_api
from .views import (
    index, reservations, profile, reset_profile_picture,
     contact, event_list, event_detail, menu,
    CustomSignupView
)

urlpatterns = [
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('profile/reset-picture/', reset_profile_picture, name='reset_profile_picture'),
    path('reservations/', reservations, name='reservations'),
    path('contact/', contact, name='contact'),
    path('events/', event_list, name='event_list'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('api/users/<int:user_id>/profile/', user_profile_api, name='user_profile_api'),
    path('menu/', menu, name='menu'),
]
