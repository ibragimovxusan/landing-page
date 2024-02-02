from .models import CatchUser
from django.contrib import messages
from django.http import JsonResponse

def update_field_to_true(request):
    # Assuming you have a condition to select the user you want to update
    # For example, let's say you want to update the field for the currently logged-in user
    if request.user.is_authenticated:
        # Update the field from False to True
        user = request.user
        user.enter_the_vebinar = True
        user.save()
        # Optionally, you can add a success message using Django messages framework
        messages.success(request, "Field updated successfully!")
    else:
        # Handle the case where the user is not authenticated
        messages.error(request, "User not authenticated!")
    # Redirect the user back to the page where the update was triggered
    return {}
