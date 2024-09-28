from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .api import user_profile_api

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('profile/', views.profile, name='profile'),
    path('accounts/delete/', views.delete_account,
         name='delete_account'),
    path('profile/reset-picture/', views.reset_profile_picture,
         name='reset_profile_picture'),

    path('reservations/', views.reservations,
         name='reservations_list'),
    path('reservations/<int:reservation_id>/',
         views.reservations, name='reservations_detail'),
    path('reservations/edit/<int:reservation_id>/',
         views.edit_reservation, name='edit_reservation'),
    path('reservations/delete/<int:reservation_id>/',
         views.delete_reservation, name='delete_reservation'),
    path('get-availability/', views.get_availability,
         name='get_availability'),

    path('contact/', views.contact, name='contact'),

    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/', views.event_detail,
         name='event_detail'),

    path('accounts/signup/', views.CustomSignupView.as_view(),
         name='account_signup'),
    path('api/v1/users/<int:user_id>/profile/',
         user_profile_api, name='user_profile_api'),

    path('menu/', views.menu, name='menu'),

    path('', views.index, name='index'),
]
