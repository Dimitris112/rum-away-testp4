from django.urls import path
from . import views

urlpatterns = [
    path('testimonials/', views.testimonial_list, name='testimonial_list'),
    path('testimonials/add/', views.add_testimonial, name='add_testimonial'),
]
