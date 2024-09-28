from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_testimonial, name='add_testimonial'),
    path(
        'edit/<int:pk>/', views.edit_testimonial,
        name='edit_testimonial'
    ),
    path(
        'delete/<int:pk>/', views.delete_testimonial,
        name='delete_testimonial'
    ),
    path(
        'detail/<int:pk>/', views.testimonial_detail,
        name='testimonial_detail'
    ),

    path(
        '<int:testimonial_id>/add-comment/',
        views.add_comment,
        name='add_comment'
    ),
    path(
        'comment/edit/<int:comment_id>/',
        views.edit_comment,
        name='edit_comment'
    ),
    path(
        'comment/delete/<int:comment_id>/',
        views.delete_comment,
        name='delete_comment'
    ),

    path('', views.testimonial_list, name='testimonial_list'),
]
