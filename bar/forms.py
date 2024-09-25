from django import forms
from .models import Reservation, Comment, UserProfile, Event, User
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

def validate_image_format(value):
    """
    Validate the format of an uploaded image.

    Args:
        value: The file or URL of the image to validate.

    Raises:
        ValidationError: If the image file type is unsupported.
    """
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


class UserProfileForm(forms.ModelForm):
    """Form for user profile data including bio and featured image."""

    class Meta:
        model = UserProfile
        fields = ['bio', 'featured_image']
        
    def clean_featured_image(self):
        """
        Validate the featured image of the user profile.

        Raises:
            ValidationError: If the image type is unsupported.
        """
        image = self.cleaned_data.get('featured_image')
        
        if image:
            if hasattr(image, 'format'):
                valid_formats = ['jpeg', 'png', 'gif', 'webp']
                if image.format.lower() not in valid_formats:
                    raise forms.ValidationError("Unsupported file type.")
            else:
                if image.content_type not in ['image/jpeg', 'image/png', 'image/webp']:
                    raise forms.ValidationError("Unsupported file type.")

        return image



class UserForm(forms.ModelForm):
    """Form for user data including first name, last name, and email."""

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_first_name(self):
        """Validate that the first name is not empty."""
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("This field is required.")
        return first_name

    def clean_last_name(self):
        """Validate that the last name is not empty."""
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("This field is required.")
        return last_name

    def clean_email(self):
        """Validate that the email is not empty."""
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("This field is required.")
        return email


class ReservationForm(forms.ModelForm):
    """Form for creating reservations including guest details and date/time."""

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
        fields = ['name', 'special_requests', 'num_guests', 'hall', 'reservation_date', 'reservation_hour', 'reservation_minute']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'special_requests': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Any special requests?'}),
            'num_guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'hall': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        """
        Validate the reservation details including time.

        Raises:
            ValidationError: If the reservation time is in the past or if 
                             hour and minute are not selected.
        """
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


class EventForm(forms.ModelForm):
    """Form for creating events including title, description, date, and image."""

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'start_time', 'end_time', 'recurrence', 'recurrence_day', 'image']
    
    def clean_image(self):
        """
        Validate the event image.

        Raises:
            ValidationError: If the image type is unsupported.
        """
        image = self.cleaned_data.get('image')
        if image:
            if not image.content_type in ['image/jpeg', 'image/png']:
                raise forms.ValidationError("Unsupported file type.")
        return image


class CommentForm(forms.ModelForm):
    """Form for submitting comments."""

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Leave a comment...'}),
        }

    def clean_content(self):
        """
        Validate the content of the comment.

        Raises:
            ValidationError: If the comment content is empty.
        """
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError('Comment cannot be empty.')
        return content