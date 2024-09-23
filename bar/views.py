from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import UserProfile, Event, Category, ContactMessage, Reservation
from .forms import UserForm, UserProfileForm, ReservationForm
from allauth.account.views import SignupView, LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.templatetags.static import static
from django.utils import timezone
from django.contrib import messages
from django.views.generic import TemplateView
from django.http import JsonResponse
from datetime import datetime, time
from django.db.models import Sum


# Sign Up
class CustomSignupView(SignupView):
    def form_valid(self, form):
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')

        if password1 != password2:
            messages.error(self.request, "Passwords do not match.")
            return self.render_to_response(self.get_context_data(form=form))

        response = super().form_valid(form)
        return redirect(reverse_lazy('index'))

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field.capitalize()}: {error}")

        return self.render_to_response(self.get_context_data(form=form))


# Sign In

class CustomLoginView(LoginView):
    def form_valid(self, form):
        username = form.cleaned_data.get('username').lower()
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            messages.error(self.request, "Invalid username or password.")
            return self.form_invalid(form)


# Home

def index(request):
    context = {
        'page_title': 'Home',
    }
    return render(request, 'bar/index.html', context)


# Make reservation

@login_required
def reservations(request, reservation_id=None):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation_date = form.cleaned_data.get('reservation_date')
            reservation_hour = form.cleaned_data.get('reservation_hour')
            reservation_minute = form.cleaned_data.get('reservation_minute')

            try:
                reservation_hour = int(reservation_hour)
                reservation_minute = int(reservation_minute)
            except (ValueError, TypeError) as e:
                messages.error(request, f"Error converting time: {e}")
                return render(request, 'bar/reservations.html', {'form': form})

            if reservation_date and reservation_hour is not None and reservation_minute is not None:
                reservation_time = timezone.make_aware(
                    datetime.combine(
                        reservation_date,
                        time(reservation_hour, reservation_minute)
                    )
                )

                if reservation_time < timezone.now():
                    messages.error(request, "Reservation time cannot be in the past.")
                    return render(request, 'bar/reservations.html', {'form': form})

                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.reservation_time = reservation_time
                reservation.save()

                messages.success(request, "Your reservation has been made successfully!")
                return render(request, 'bar/reservations.html', {'reservation': reservation})
            else:
                messages.error(request, "Please select a valid date and time.")
    else:
        form = ReservationForm()

    upcoming_reservations = Reservation.objects.filter(user=request.user, reservation_time__gte=timezone.now()).order_by('reservation_time')

    reservation = None
    if reservation_id:
        reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)

    context = {
        'page_title': 'Reservations',
        'form': form,
        'upcoming_reservations': upcoming_reservations,
        'reservation': reservation,
    }
    return render(request, 'bar/reservations.html', context)



# Edit reservation

@login_required
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            reservation.edited = True
            reservation.save()
            messages.success(request, "Your reservation has been updated successfully!")
            return redirect('profile')
    else:
        form = ReservationForm(instance=reservation)

    context = {
        'form': form,
        'reservation': reservation,
        'page_title': 'Edit Reservation',
    }
    return render(request, 'bar/edit_reservation.html', context)


# Delete reservation

@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    reservation.delete()
    messages.success(request, "Your reservation has been deleted successfully!")
    return redirect('profile')


@login_required
def profile(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)

    upcoming_reservations = Reservation.objects.filter(user=request.user, reservation_time__gte=timezone.now()).order_by('reservation_time')

    context = {
        'page_title': 'Profile',
        'user_form': user_form,
        'profile_form': profile_form,
        'upcoming_reservations': upcoming_reservations,
    }
    return render(request, 'bar/profile.html', context)


# Reset pfp

@login_required
@require_POST
def reset_profile_picture(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    profile.featured_image = None
    profile.save()
    return redirect('profile')


# Send contact msg

def contact(request):
    form_data = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')

        if not name:
            messages.error(request, "Name is required.")
        elif not email:
            messages.error(request, "Email is required.")
        elif not message_content:
            messages.error(request, "Message cannot be empty.")
        else:
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message_content
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')

        form_data = {
            'name': name,
            'email': email,
            'message': message_content,
        }

    context = {
        'page_title': 'Contact Us',
        'form_data': form_data,
    }
    return render(request, 'bar/contact.html', context)


# Events

def event_list(request):
    now = timezone.now()
    events = Event.objects.filter(date__gte=now).order_by('date')
    context = {
        'page_title': 'Events',
        'events': events,
    }
    return render(request, 'bar/event_list.html', context)


# Specific event

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'page_title': event.title,
        'event': event
    }
    return render(request, 'bar/event_detail.html', context)


# Menu

def menu(request):
    categories = ["Wines", "Beers", "Whiskey", "Vodka", "Rum", "Cocktails"]
    context = {
        'page_title': 'Menu',
        'categories': categories,
    }
    return render(request, 'bar/menu.html', context)


# spots available

def calculate_spots_left(hall, reservation_datetime):
    max_capacity = 70 if hall == 'indoor' else 120

    reservations = Reservation.objects.filter(
        hall=hall,
        reservation_time__date=reservation_datetime.date(),
        reservation_time__hour=reservation_datetime.hour,
    )

    total_guests = sum(reservation.num_guests for reservation in reservations)
    spots_left = max_capacity - total_guests

    return spots_left, max_capacity



def get_availability(request):
    hall = request.GET.get('hall')
    reservation_time = request.GET.get('reservation_time')

    if not hall or not reservation_time:
        return JsonResponse({'error': 'Missing hall or reservation_time parameter'}, status=400)

    try:
        reservation_datetime = timezone.datetime.fromisoformat(reservation_time)
    except ValueError:
        return JsonResponse({'error': 'Invalid date format'}, status=400)

    if hall == 'indoor':
        max_capacity = 70
    elif hall == 'outdoor':
        max_capacity = 120
    else:
        return JsonResponse({'error': 'Invalid hall type'}, status=400)

    spots_left = calculate_spots_left(hall, reservation_datetime)

    return JsonResponse({
        'spots_left': spots_left,
        'max_capacity': max_capacity
    })