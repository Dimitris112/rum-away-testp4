from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation, Order, Comment, UserProfile
from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserForm

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

@login_required
def profile(request):
    # Ensure the user has a UserProfile - create one if they don't
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    context = {
        'page_title': 'Profile',
        'user_form': user_form,
        'profile_form': profile_form,
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
