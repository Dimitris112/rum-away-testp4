from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import UserProfile, Event, Category, ContactMessage, Reservation
from .forms import UserForm, UserProfileForm
from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.templatetags.static import static
from django.utils import timezone
from django.contrib import messages

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(reverse_lazy('index'))

def index(request):
    context = {
        'page_title': 'Home',
    }
    return render(request, 'bar/index.html', context)

@login_required
def reservations(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, "Your reservation has been made successfully!")
            return redirect('profile')
    else:
        form = ReservationForm()
    
    context = {
        'page_title': 'Reservations',
        'form': form,
    }
    return render(request, 'bar/contact.html', context)


@login_required
def profile(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)

    # upcoming reservations
    upcoming_reservations = Reservation.objects.filter(user=request.user, reservation_time__gte=timezone.now()).order_by('reservation_time')

    context = {
        'page_title': 'Profile',
        'user_form': user_form,
        'profile_form': profile_form,
        'upcoming_reservations': upcoming_reservations,
    }
    return render(request, 'bar/profile.html', context)



@login_required
@require_POST
def reset_profile_picture(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    profile.featured_image = None
    profile.save()
    return redirect('profile')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message_content
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    context = {
        'page_title': 'Contact Us',
    }
    return render(request, 'bar/contact.html', context)


def event_list(request):
    now = timezone.now()
    events = Event.objects.filter(date__gte=now).order_by('date')
    context = {
        'page_title': 'Events',
        'events': events,
    }
    return render(request, 'bar/event_list.html', context)

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'page_title': event.title,
        'event': event
    }
    return render(request, 'bar/event_detail.html', context)

def menu(request):
    categories = ["Wines", "Beers", "Whiskey", "Vodka", "Rum", "Cocktails"]
    context = {
        'page_title': 'Menu',
        'categories': categories,
    }
    return render(request, 'bar/menu.html', context)
