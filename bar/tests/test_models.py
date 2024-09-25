from django.test import TestCase
from .models import Reservation, Comment, UserProfile, Event, ContactMessage, Category
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
