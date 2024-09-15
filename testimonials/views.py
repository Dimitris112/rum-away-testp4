from django.shortcuts import render, redirect
from .forms import TestimonialForm
from .models import Testimonial

def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})

def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
    else:
        form = TestimonialForm()
    
    return render(request, 'testimonials/add_testimonial.html', {'form': form})
