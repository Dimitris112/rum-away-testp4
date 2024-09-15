from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm
from .models import Testimonial

def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})

@login_required
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
    else:
        form = TestimonialForm(user=request.user)
    
    return render(request, 'testimonials/add_testimonial.html', {'form': form})