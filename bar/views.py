from django.shortcuts import render, get_object_or_404
from .models import Reservation, Order, Comment, UserProfile
from allauth.account.views import SignupView
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('/')

def index(request):
    context = {
        'page_title': 'Home',
    }
    return render(request, 'bar/index.html', context)

def reservations(request):
    context = {
        'page_title': 'Reservations',
    }
    return render(request, 'bar/reservations.html', context)

def profile(request):
    context = {
        'page_title': 'Profile',
    }
    return render(request, 'bar/profile.html', context)

def orders(request):
    context = {
        'page_title': 'Orders',
    }
    return render(request, 'bar/orders.html', context)

def comments(request):
    context = {
        'page_title': 'Comments',
    }
    return render(request, 'bar/comments.html', context)  
