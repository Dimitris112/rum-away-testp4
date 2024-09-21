from django.http import JsonResponse
from .models import UserProfile
from django.contrib.auth.decorators import login_required

@login_required
def user_profile_api(request, user_id):
    try:
        profile = UserProfile.objects.get(user__id=user_id)
        data = {
            'username': profile.user.username,
            'bio': profile.bio,
            'profile_picture': profile.get_profile_picture_url(),
            'member_since': profile.user.date_joined.strftime("%Y-%m-%d"),
        }
        return JsonResponse(data)
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'User profile not found'}, status=404)

# cross towards bar and testimonial app
# open new modal in testimonial_list.html for user profile card