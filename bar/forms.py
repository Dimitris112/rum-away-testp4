from django import forms
from .models import Reservation, Comment, UserProfile, Event, User
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime


# Validation for image formats
def validate_image_format(value):
    valid_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp']
    
    if hasattr(value, 'name'):
        if not any(value.name.lower().endswith(ext) for ext in valid_extensions):
            raise ValidationError('Unsupported file extension. Allowed extensions are: png, jpg, jpeg, gif, webp.')
    
    elif hasattr(value, 'url'):
        file_url = value.url.lower()
        if not any(file_url.endswith(ext) for ext in valid_extensions):
            raise ValidationError('Unsupported file extension. Allowed extensions are: png, jpg, jpeg, gif, webp.')
    
    else:
        raise ValidationError('Unsupported file type.')


# Form to handle profile update

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['featured_image', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us about yourself...'}),
        }

    def clean_featured_image(self):
        image = self.cleaned_data.get('featured_image')
        if image:
            validate_image_format(image)
        return image



# Form to handle user data update

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


# Form for making a reservation

class ReservationForm(forms.ModelForm):
    reservation_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label="Date of Reservation"
    )
    reservation_hour = forms.ChoiceField(
        choices=[(str(i), f"{i:02d}") for i in range(24)],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Hour of Reservation"
    )
    reservation_minute = forms.ChoiceField(
        choices=[(str(i), f"{i:02d}") for i in range(0, 60, 5)],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Minute of Reservation"
    )

    class Meta:
        model = Reservation
        fields = ['name', 'special_requests', 'num_guests', 'hall']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'special_requests': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Any special requests?'}),
            'num_guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'hall': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        reservation_date = cleaned_data.get('reservation_date')
        reservation_hour = cleaned_data.get('reservation_hour')
        reservation_minute = cleaned_data.get('reservation_minute')

        if not reservation_hour or not reservation_minute:
            raise ValidationError('Please select both the hour and minute for the reservation.')

        try:
            reservation_hour = int(reservation_hour)
            reservation_minute = int(reservation_minute)
        except (ValueError, TypeError):
            raise ValidationError('Invalid hour or minute selected.')

        if reservation_date:
            reservation_time = timezone.make_aware(
                datetime.datetime.combine(
                    reservation_date,
                    datetime.time(reservation_hour, reservation_minute)
                )
            )

            if reservation_time < timezone.now():
                self.add_error('reservation_date', 'Reservation time cannot be in the past.')

            cleaned_data['reservation_time'] = reservation_time

        return cleaned_data



# Form for creating or updating events

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'start_time', 'end_time', 'image', 'recurrence', 'recurrence_day']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'recurrence': forms.Select(attrs={'class': 'form-control'}),
            'recurrence_day': forms.Select(attrs={'class': 'form-control'}),
        }
