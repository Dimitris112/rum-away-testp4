from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm, CommentForm
from .models import Testimonial, Comment
from django.utils import timezone
from django.utils.decorators import method_decorator
import json

# all testimonials

def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})

# add testimonial

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


# edit testimonial

@login_required
def edit_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)

    if request.user != testimonial.user:
        messages.error(request, 'You do not have permission to edit this testimonial.')
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

    return render(request, 'testimonials/edit_testimonial.html', {'form': form, 'testimonial': testimonial})



# delete testimonial

@login_required
def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)

    if request.user == testimonial.user or request.user.is_superuser:
        if request.method == 'POST':
            testimonial.delete()
            messages.success(request, 'Testimonial deleted successfully.')
            return redirect('testimonial_list')
    else:
        messages.error(request, 'You do not have permission to delete this testimonial.')
        return redirect('testimonial_list')
    
    return render(request, 'testimonials/delete_testimonial.html', {'testimonial': testimonial})



#add comment

@require_POST
@login_required
def add_comment(request, testimonial_id):
    try:
        # Parse the request body to get the comment content
        data = json.loads(request.body)
        content = data.get('content')

        if not content:
            return JsonResponse({'success': False, 'error': 'Comment content cannot be empty'}, status=400)

        testimonial = get_object_or_404(Testimonial, id=testimonial_id)

        comment = Comment.objects.create(
            content=content,
            testimonial=testimonial,
            user=request.user
        )

        return JsonResponse({
            'success': True,
            'user_name': request.user.username,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })

    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


# edit comment

@require_POST
@login_required
def edit_comment(request, comment_id):
    try:
        comment = get_object_or_404(Comment, id=comment_id, user=request.user)
        content = json.loads(request.body).get('content')

        if not content:
            return JsonResponse({'success': False, 'error': 'Comment content cannot be empty'}, status=400)

        if len(content) > 50: 
            return JsonResponse({'success': False, 'error': 'Comment cannot exceed 50 characters'}, status=400)

        comment.content = content
        comment.was_edited = True
        comment.save()

        return JsonResponse({'success': True, 'testimonial_id': comment.testimonial.id, 'was_edited': comment.was_edited})

    except Comment.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Comment not found.'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)




# delete comment

@login_required
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.user or request.user.is_superuser:
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'You do not have permission to delete this comment.'}, status=403)



# T E S T 


def testimonial_detail(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    comments = testimonial.comments.all()
    return render(request, 'testimonials/testimonial_detail.html', {
        'testimonial': testimonial,
        'comments': comments,
    })

@login_required
def load_more_comments(request, testimonial_id):
    if request.method == 'GET':
        testimonial = get_object_or_404(Testimonial, id=testimonial_id)
        offset = int(request.GET.get('offset', 3))
        comments = testimonial.comments.all()[offset:offset + 3]

        return JsonResponse({
            'comments': [
                {
                    'user_name': comment.user.username,
                    'content': comment.content,
                    'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
                } for comment in comments
            ],
            'total_count': testimonial.comments.count()
        })
