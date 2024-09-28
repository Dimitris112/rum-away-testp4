from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm, CommentForm
from .models import Testimonial, Comment
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.db.models import Count
import json


# all testimonials
def testimonial_list(request):
    """
    Display a list of testimonials sorted by the specified option.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template with sorted testimonials.
    """
    sort_option = request.GET.get('sort', 'date')

    if sort_option == 'views':
        testimonials = Testimonial.objects.annotate(
            num_comments=Count('comments')
        ).order_by('-views_count', '-num_comments', '-rating')
    elif sort_option == 'comments':
        testimonials = Testimonial.objects.annotate(
            num_comments=Count('comments')
        ).order_by('-num_comments', '-views_count', '-rating')
    elif sort_option == 'rating':
        testimonials = Testimonial.objects.annotate(
            num_comments=Count('comments')
        ).order_by('-rating', '-views_count', '-num_comments')
    else:  # Default sorting by date
        testimonials = Testimonial.objects.annotate(
            num_comments=Count('comments')
        ).order_by('-created_at', '-views_count', '-num_comments', '-rating')

    return render(
        request, 'testimonials/testimonial_list.html',
        {'testimonials': testimonials}
    )


# Add testimonial
@login_required
def add_testimonial(request):
    """
    Add a new testimonial for the logged-in user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template for adding a testimonial.
    """
    if request.method == 'POST':
        form = TestimonialForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Your testimonial has been added successfully!")
            return redirect('testimonial_list')
    else:
        form = TestimonialForm(user=request.user)

    return render(
        request, 'testimonials/add_testimonial.html',
        {'form': form}
    )


# Edit testimonial
@login_required
def edit_testimonial(request, pk):
    """
    Edit an existing testimonial for the logged-in user.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the testimonial to edit.

    Returns:
        HttpResponse: Rendered template for editing a testimonial.
    """
    testimonial = get_object_or_404(Testimonial, pk=pk)

    if request.user != testimonial.user:
        messages.error(request,
                       'You do not have permission to edit this testimonial.')
        return redirect('testimonial_list')

    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.was_edited = True
            testimonial.updated_at = timezone.now()
            testimonial.save()
            messages.success(request, 'Testimonial edited successfully!')
            return redirect('testimonial_list')
    else:
        form = TestimonialForm(instance=testimonial)

    return render(
        request, 'testimonials/edit_testimonial.html',
        {'form': form, 'testimonial': testimonial}
    )


# Delete testimonial
@login_required
def delete_testimonial(request, pk):
    """
    Delete a testimonial if the user has permission.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the testimonial to delete.

    Returns:
        HttpResponse: Redirects to the testimonial list or renders a
        delete confirmation template.
    """
    testimonial = get_object_or_404(Testimonial, pk=pk)

    if request.user == testimonial.user or request.user.is_superuser:
        if request.method == 'POST':
            testimonial.delete()
            messages.success(request, 'Testimonial deleted successfully.')
            return redirect('testimonial_list')
    else:
        messages.error(request,
                       'You do not have permission to delete this '
                       'testimonial.')
        return redirect('testimonial_list')

    return render(
        request, 'testimonials/delete_testimonial.html',
        {'testimonial': testimonial}
    )


# Add comment
@require_POST
@login_required
def add_comment(request, testimonial_id):
    """
    Add a comment to a testimonial.

    Args:
        request (HttpRequest): The HTTP request object.
        testimonial_id (int): The ID of the testimonial.

    Returns:
        JsonResponse: Contains the result of the operation.
    """
    try:
        # Parse the request body to get the comment content
        data = json.loads(request.body)
        content = data.get('content')

        if not content:
            return JsonResponse({
                'success': False,
                'error': 'Comment content cannot be empty'
            }, status=400)

        testimonial = get_object_or_404(Testimonial, id=testimonial_id)

        comment = Comment.objects.create(
            content=content,
            testimonial=testimonial,
            user=request.user
        )

        return JsonResponse({
            'success': True,
            'comment_id': comment.id,
            'user_name': request.user.username,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })

    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


# Edit comment
@require_POST
@login_required
def edit_comment(request, comment_id):
    """
    Edit a comment made by the user.

    Args:
        request (HttpRequest): The HTTP request object.
        comment_id (int): The ID of the comment.

    Returns:
        JsonResponse: Contains the result of the operation.
    """
    try:
        comment = get_object_or_404(Comment, id=comment_id, user=request.user)
        content = json.loads(request.body).get('content')

        if not content:
            return JsonResponse({
                'success': False,
                'error': 'Comment content cannot be empty'
            }, status=400)

        if len(content) > 50:
            return JsonResponse({
                'success': False,
                'error': 'Comment cannot exceed 50 characters'
            }, status=400)

        comment.content = content
        comment.was_edited = True
        comment.save()

        return JsonResponse({
            'success': True,
            'comment_id': comment.id,
            'testimonial_id': comment.testimonial.id,
            'user_name': comment.user.username,
            'updated_at': comment.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            'was_edited': comment.was_edited
        })

    except Comment.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Comment not found.'
        }, status=404)
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


# Delete comment
@login_required
@require_POST
def delete_comment(request, comment_id):
    """
    Delete a comment if the user has permission.

    Args:
        request (HttpRequest): The HTTP request object.
        comment_id (int): The ID of the comment to delete.

    Returns:
        JsonResponse: Contains the result of the operation.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.user or request.user.is_superuser:
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return JsonResponse({'success': True})

    return JsonResponse({
        'success': False,
        'error': 'You do not have permission to delete this comment.'
    }, status=403)


# View testimonial
def testimonial_detail(request, pk):
    """Display a testimonial and its comments."""
    testimonial = get_object_or_404(Testimonial, pk=pk)
    testimonial.views_count += 1
    testimonial.save(update_fields=['views_count'])

    comments = testimonial.comments.all()
    return render(request, 'testimonials/testimonial_detail.html', {
        'testimonial': testimonial,
        'comments': comments,
    })