from django import forms
from .models import Testimonial, Comment


class TestimonialForm(forms.ModelForm):
    """
    Form for creating/updating Testimonial instances.

    - Fields: 'content', 'rating'
    - Automatically sets 'name' and 'user' if provided
    """

    class Meta:
        model = Testimonial
        fields = ['content', 'rating']

    def __init__(self, *args, **kwargs):
        """
        - Pops 'user' from kwargs if available
        - Initializes the form with the remaining args/kwargs
        """
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        """
        - Sets 'name' and 'user' if provided
        - Saves the Testimonial instance (optionally commit)
        - Returns the saved instance
        """
        instance = super().save(commit=False)
        if self.user:
            instance.name = self.user.username
            instance.user = self.user
        if commit:
            instance.save()
        return instance


class CommentForm(forms.ModelForm):
    """
    Form for creating/updating Comment instances.

    - Fields: 'content'
    - Uses custom Textarea widget for the 'content' field
    """

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Add your comment...',
                'rows': 3
            }),
        }
