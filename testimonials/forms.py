from django import forms
from .models import Testimonial, Comment

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['content', 'rating']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.name = self.user.username
            instance.user = self.user
        if commit:
            instance.save()
        return instance

class CommentForm(forms.ModelForm):
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