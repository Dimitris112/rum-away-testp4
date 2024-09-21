from django import forms
from .models import Reservation, Comment, UserProfile, Event, User
from django.core.exceptions import ValidationError
from django.utils import timezone


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
    class Meta:
        model = Reservation
        fields = ['name', 'reservation_time', 'special_requests', 'num_guests', 'hall']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'reservation_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
            'special_requests': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Any special requests?'}),
            'num_guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'hall': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_reservation_time(self):
        reservation_time = self.cleaned_data.get('reservation_time')
        if reservation_time and reservation_time < timezone.now():
            raise ValidationError('Reservation time cannot be in the past.')
        return reservation_time


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
