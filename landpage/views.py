import random
import string
from .models import CatchUser, Deadline
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.utils import timezone



def register(request):
    last_time = Deadline.objects.all().last()
    if last_time.datetime > timezone.now():
        print("Hello")
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            phone_number = request.POST.get('phone_number')
            password = "Pass!123"
            print(phone_number)
            print(first_name)

            user = CatchUser.objects.filter(username=phone_number)

            if user.exists():
                messages.warning(request, "User already exists!")
                return redirect('/')
            else:
                instance = CatchUser.objects.create_user(username=phone_number, password=password, first_name=first_name)
                user = authenticate(username=phone_number, password=password, first_name=first_name)
                if user is not None:
                    login(request, user)
                messages.success(request, 'Your account has been created!')
                return redirect("/")
        else:
            pass
    return render(request, 'index.html', {'date_time': last_time})



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