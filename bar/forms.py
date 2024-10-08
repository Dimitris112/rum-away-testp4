from django import forms
from .models import Reservation, Comment, UserProfile, Event, User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
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
        if not any(
            value.name.lower().endswith(ext) for ext in valid_extensions
        ):
            raise ValidationError(
                'Unsupported file extension. Allowed extensions are: png, '
                'jpg, jpeg, gif, webp.'
            )
    elif hasattr(value, 'url'):
        file_url = value.url.lower()
        if not any(
            file_url.endswith(ext) for ext in valid_extensions
        ):
            raise ValidationError(
                'Unsupported file extension. Allowed extensions are: png, '
                'jpg, jpeg, gif, webp.'
            )
    else:
        raise ValidationError('Unsupported file type.')


class UserProfileForm(forms.ModelForm):
    """Form for user profile data including bio and featured image."""
    bio = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control shadow-sm',
            'placeholder': 'Tell us about yourself...',
            'oninput': 'updateBioCount(this)',
            'maxlength': 50
        })
    )

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
                if image.content_type not in [
                    'image/jpeg', 'image/png', 'image/gif', 'image/webp'
                ]:
                    raise forms.ValidationError("Unsupported file type.")

        return image


class UserForm(forms.ModelForm):
    """Form for user data including first name, last name, and email."""

    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control shadow-sm',
        'placeholder': 'First Name',
        'maxlength': 30
    }))

    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control shadow-sm',
        'placeholder': 'Last Name',
        'maxlength': 30
    }))

    email = forms.EmailField(max_length=35, widget=forms.EmailInput(attrs={
        'class': 'form-control shadow-sm',
        'placeholder': 'Email',
        'maxlength': 35
    }))

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
        """Validate that the email is not empty and is valid."""
        email = self.cleaned_data.get('email')
        email_validator = EmailValidator()

        if not email:
            raise forms.ValidationError("This field is required.")
        try:
            email_validator(email)
        except ValidationError:
            raise forms.ValidationError("Enter a valid email.")

        return email


class ReservationForm(forms.ModelForm):
    """Form for creating reservations including guest details and date/time."""

    reservation_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
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
        fields = [
            'name', 'special_requests', 'num_guests', 'hall',
            'reservation_date', 'reservation_hour', 'reservation_minute'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'special_requests': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Any special requests?'
            }),
            'num_guests': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
            'hall': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        """
        Validate the reservation details and check for existing reservations.

        Raises:
            ValidationError: If the user already has a reservation on the same
            date or if the reservation time is in the past.
        """
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get('reservation_date')
        reservation_hour = cleaned_data.get('reservation_hour')
        reservation_minute = cleaned_data.get('reservation_minute')

        if not reservation_hour or not reservation_minute:
            raise ValidationError(
                'Please select both the hour and minute for the reservation.'
            )

        if reservation_date:
            # Combine the date, hour, and minute into a single datetime
            reservation_time = timezone.make_aware(
                datetime.datetime.combine(
                    reservation_date,
                    datetime.time(
                        int(reservation_hour),
                        int(reservation_minute)
                    )
                )
            )

            if reservation_time < timezone.now():
                raise ValidationError(
                    "Reservation time cannot be in the past."
                )

            user = self.instance.user if self.instance.pk else None

            if user:
                same_day_reservations = Reservation.objects.filter(
                    user=user,
                    reservation_time__date=reservation_date
                ).exclude(pk=self.instance.pk)

                if same_day_reservations.exists():
                    raise ValidationError(
                        "You already have a reservation on this date."
                    )

        return cleaned_data


class EventForm(forms.ModelForm):
    """Form for creating events, including title, description, date,
    and image."""

    class Meta:
        model = Event
        fields = [
            'title', 'description', 'date', 'start_time', 'end_time',
            'recurrence', 'recurrence_day', 'image'
        ]

    def clean_image(self):
        """Validate the event image."""
        image = self.cleaned_data.get('image')
        if image:
            if image.content_type not in ['image/jpeg', 'image/png']:
                raise forms.ValidationError("Unsupported file type.")
        return image


class CommentForm(forms.ModelForm):
    """Form for submitting comments."""

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Leave a comment...'
            }),
        }

    def clean_content(self):
        """Validate the content of the comment."""
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError('Comment cannot be empty.')
        return content
