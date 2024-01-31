import random
import string
from .models import CatchUser, Deadline
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from datetime import datetime



def register(request):
    usernames = CatchUser.objects.values_list('username', flat=True)
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['username']
        password = "Pass!123"

        user = CatchUser.objects.filter(username=phone_number)

        if user.exists():
            messages.warning(request, "User already exists!")
            return redirect('register')
        else:
            instance = CatchUser.objects.create_user(username=phone_number, password=password, first_name=first_name,
                                                    last_name=last_name, phone_number=phone_number)
            user = authenticate(username=phone_number, password=password, first_name=first_name, last_name=last_name, phone_number=phone_number)
            if user is not None:
                login(request, user)
            messages.success(request, 'Your account has been created!')
            return redirect("/")
    print("Success")
    return render(request, 'index.html')



# from datetime import datetime

# def index(request):
#     last_deadline = Deadline.objects.all().last()

#     if last_deadline:
#         deadline_time = last_deadline.deadline_time
#         current_datetime = datetime.now()

#         if deadline_time > current_datetime:
#             register(request)
#         elif deadline_time < current_datetime:
#             user = request.user
#             if user.is_authenticated:
#                 user.enter_the_vebinar = True
#                 user.save()
#             return redirect('/')
#         else:
#             return redirect('/')

#     return render(request, 'index.html')

    last_datetime = Deadline.objects.all().last()
    current_datetime = datetime.now()

    if last_datetime > current_datetime:
        register(request)
    elif last_datetime < current_datetime:
        user = request.user
        if user.is_authenticated:
            user.enter_the_vebinar = True
            user.save()
        return redirect('/')
    else:
        return redirect('/')

    return render(request, 'index.html')