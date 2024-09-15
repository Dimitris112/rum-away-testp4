from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm
from .models import Testimonial
from django.utils import timezone

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

@login_required
def edit_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            testimonial.updated_at = timezone.now()
            testimonial.save()
            messages.success(request, 'Testimonial edited successfully!')
            return redirect('testimonial_list')
    else:
        form = TestimonialForm(instance=testimonial)
    
    return render(request, 'testimonials/edit_testimonial.html', {'form': form, 'testimonial': testimonial})


@login_required
def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk, user=request.user)
    if request.method == 'POST':
        testimonial.delete()
        return redirect('testimonial_list')
    
    return render(request, 'testimonials/delete_testimonial.html', {'testimonial': testimonial})
